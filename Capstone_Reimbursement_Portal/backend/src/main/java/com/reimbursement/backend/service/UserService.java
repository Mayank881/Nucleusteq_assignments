package com.reimbursement.backend.service;

import com.reimbursement.backend.constants.Messages;
import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.mapper.UserMapper;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * handles user related business logic
 */
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

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
                .orElseThrow(() -> new ResourceNotFoundException(Messages.EMPLOYEE_NOT_FOUND));

        User manager = userRepository.findById(managerId)
                .orElseThrow(() -> new ResourceNotFoundException(Messages.MANAGER_NOT_FOUND));

        employee.setManager(manager);

        User savedUser = userRepository.save(employee);

        return UserMapper.toDTO(savedUser);
    }
}
