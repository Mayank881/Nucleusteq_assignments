package com.reimbursement.backend.service;

import com.reimbursement.backend.constants.Messages;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.mapper.UserMapper;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.dto.logindto.LoginRequestDTO;
import com.reimbursement.backend.entity.Claim;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;
import com.reimbursement.backend.repository.ClaimRepository;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import com.reimbursement.backend.config.JwtUtil;
import com.reimbursement.backend.dto.logindto.LoginResponseDTO;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import java.util.Map;

import java.util.List;

/**
 * handles user related business logic
 */
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private ClaimRepository claimRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private JwtUtil jwtUtil;

    /**
     * create a new user
     */
    public UserResponseDTO createUser(UserRequestDTO requestDTO) {

        // email validation
        if (userRepository.existsByEmail(requestDTO.getEmail())) {
            throw new BadRequestException(Messages.EMAIL_EXISTS);
        }

        if (!requestDTO.getEmail().endsWith("@company.com")) {
            throw new BadRequestException(Messages.INVALID_EMAIL_DOMAIN);
        }

        // map DTO to entity and save
        User user = UserMapper.toEntity(requestDTO);

        // hash password before saving
        user.setPassword(passwordEncoder.encode(user.getPassword()));

        User savedUser = userRepository.save(user);
        return UserMapper.toDTO(savedUser);
    }

    /**
     * get all users
     */
    public Map<String, Object> getAllUsers(int page, int size) {

        Pageable pageable = PageRequest.of(page, size);

        Page<User> userPage = userRepository.findAll(pageable);

        List<UserResponseDTO> userList = userPage.getContent()
                .stream()
                .map(UserMapper::toDTO)
                .toList();

        return Map.of(
                "content", userList,
                "page", userPage.getNumber(),
                "size", userPage.getSize(),
                "totalElements", userPage.getTotalElements(),
                "totalPages", userPage.getTotalPages());
    }

    /**
     * assign manager to employee
     */
    @Transactional
    public UserResponseDTO assignManager(Long employeeId, Long managerId) {

        User employee = userRepository.findById(employeeId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.EMPLOYEE_NOT_FOUND));

        User manager = userRepository.findById(managerId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.MANAGER_NOT_FOUND));

        if (!"EMPLOYEE".equals(employee.getRole().name())) {
            throw new BadRequestException("Selected user is not an employee");
        }

        if (!"MANAGER".equals(manager.getRole().name())) {
            throw new BadRequestException("Selected user is not a manager");
        }

        employee.setManager(manager);
        userRepository.save(employee);

        // reassign OLD claims
        List<Claim> claims = claimRepository.findByEmployeeId(employeeId);

        for (Claim c : claims) {

            if (c.getStatus().name().equals("SUBMITTED")) {
                c.setReviewer(manager);
            }
        }

        claimRepository.saveAll(claims);

        return UserMapper.toDTO(employee);
    }

    /**
     * delete user safely
     */

    @Transactional
    public void deleteUser(Long userId) {

        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.USER_NOT_FOUND));

        if ("ADMIN".equals(user.getRole().name())) {
            throw new BadRequestException(Messages.ADMIN_CANT_DELETED);
        }

        // find admin
        User admin = userRepository.findAll()
                .stream()
                .filter(u -> u.getRole().name().equals("ADMIN"))
                .findFirst()
                .orElseThrow(() -> new ResourceNotFoundException("Admin not found"));

        if ("EMPLOYEE".equals(user.getRole().name())) {

            // delete employee claims
            claimRepository.deleteByEmployee(user);

        }

        if ("MANAGER".equals(user.getRole().name())) {

            // reassign employees to admin
            List<User> users = userRepository.findAll();
            for (User u : users) {
                if (u.getManager() != null && u.getManager().getId().equals(userId)) {
                    u.setManager(admin);
                }
            }

            // reassign claims to admin
            List<Claim> claims = claimRepository.findByReviewerId(userId);

            for (Claim c : claims) {
                c.setReviewer(admin);
            }

            claimRepository.saveAll(claims);
        }

        userRepository.delete(user);
    }

    /**
     * login user and return JWT token
     */
    public LoginResponseDTO login(LoginRequestDTO request) {

        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new ResourceNotFoundException(Messages.USER_NOT_FOUND));

        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            throw new BadRequestException("invalid password");
        }

        String token = jwtUtil.generateToken(user.getEmail());
        return new LoginResponseDTO(
                token,
                user.getId(),
                user.getEmail(),
                user.getRole().name());
    }

}
