package com.reimbursement.backend.service;

import com.reimbursement.backend.constants.Messages;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.mapper.UserMapper;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.dto.logindto.LoginRequestDTO;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;
import com.reimbursement.backend.repository.ClaimRepository;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
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
    public UserResponseDTO assignManager(Long employeeId, Long managerId) {

        User employee = userRepository.findById(employeeId)
                .orElseThrow(() -> new ResourceNotFoundException("Selected user is not an employee"));

        User manager = userRepository.findById(managerId)
                .orElseThrow(() -> new ResourceNotFoundException("Selected user is not a manager"));

        // null safety
        if (employee.getRole() == null || manager.getRole() == null) {
            throw new BadRequestException("User roles must be defined");
        }

        // role validation
        if (!"EMPLOYEE".equals(employee.getRole().name())) {
            throw new BadRequestException("Selected user is not an employee");
        }

        if (!"MANAGER".equals(manager.getRole().name())) {
            throw new BadRequestException("Selected user is not a manager");
        }

        if (employeeId.equals(managerId)) {
            throw new BadRequestException("Employee cannot be their own manager");
        }

        employee.setManager(manager);

        User savedUser = userRepository.save(employee);

        return UserMapper.toDTO(savedUser);
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

        // remove manager references
        List<User> users = userRepository.findAll();
        for (User u : users) {
            if (u.getManager() != null && u.getManager().getId().equals(userId)) {
                u.setManager(null);
            }
        }

        claimRepository.deleteByEmployee(user);
        claimRepository.deleteByReviewer(user);

        userRepository.delete(user);
    }

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
