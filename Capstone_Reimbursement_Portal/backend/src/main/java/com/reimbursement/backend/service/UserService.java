package com.reimbursement.backend.service;

import com.reimbursement.backend.constants.Messages;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.mapper.UserMapper;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;
import com.reimbursement.backend.repository.ClaimRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
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

        User savedUser = userRepository.save(user);

        return UserMapper.toDTO(savedUser);
    }

    /**
     * get all users
     */
    public List<UserResponseDTO> getAllUsers() {

        List<User> users = userRepository.findAll();

        List<UserResponseDTO> responseList = new ArrayList<>();

        for (User user : users) {
            responseList.add(UserMapper.toDTO(user));
        }

        return responseList;
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

        // prevent self assignment
        if (employeeId.equals(managerId)) {
            throw new BadRequestException("Employee cannot be their own manager");
        }

        // assign manager
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

        // delete claims safely
        claimRepository.deleteByEmployee(user);
        claimRepository.deleteByReviewer(user);

        userRepository.delete(user);
    }
}