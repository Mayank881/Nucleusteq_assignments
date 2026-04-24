package com.reimbursement.backend.service;

import com.reimbursement.backend.exception.BadRequestException;
import com.reimbursement.backend.exception.ResourceNotFoundException;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


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

        if (userRepository.existsByEmail(requestDTO.getEmail())) {
           throw new BadRequestException("Email already exists");
        }

        if (!requestDTO.getEmail().endsWith("@company.com")) {
            throw new BadRequestException("Email must be a company email (@company.com)");
        }

        User user = new User();
        user.setName(requestDTO.getName());
        user.setEmail(requestDTO.getEmail());
        user.setPassword(requestDTO.getPassword());
        user.setRole(requestDTO.getRole());

        User savedUser = userRepository.save(user);

        UserResponseDTO responseDTO = new UserResponseDTO();
        responseDTO.setId(savedUser.getId());
        responseDTO.setName(savedUser.getName());
        responseDTO.setEmail(savedUser.getEmail());
        responseDTO.setRole(savedUser.getRole());

        return responseDTO;
    }

    /**
     * get all users
     */
    public List<UserResponseDTO> getAllUsers() {

        List<User> users = userRepository.findAll();

        List<UserResponseDTO> responseList = new java.util.ArrayList<>();

        for (User user : users) {

            UserResponseDTO dto = new UserResponseDTO();
            dto.setId(user.getId());
            dto.setName(user.getName());
            dto.setEmail(user.getEmail());
            dto.setRole(user.getRole());

            responseList.add(dto);
        }

        return responseList;
    }

    /**
     * assign manager to employee
     */
    public UserResponseDTO assignManager(Long employeeId, Long managerId) {

        User employee = userRepository.findById(employeeId)
              .orElseThrow(() -> new ResourceNotFoundException("Employee not found"));

        User manager = userRepository.findById(managerId)
                .orElseThrow(() -> new ResourceNotFoundException("Manager not found"));

        employee.setManager(manager);

        User savedUser = userRepository.save(employee);

        UserResponseDTO dto = new UserResponseDTO();
        dto.setId(savedUser.getId());
        dto.setName(savedUser.getName());
        dto.setEmail(savedUser.getEmail());
        dto.setRole(savedUser.getRole());

        return dto;
    }
}