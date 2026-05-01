package com.reimbursement.backend.mapper;

import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.entity.User;

/**
 * handles mapping between User and DTOs 
 */
public class UserMapper {

    public static User toEntity(UserRequestDTO dto) {

        User user = new User();
        user.setName(dto.getName());
        user.setEmail(dto.getEmail());
        user.setPassword(dto.getPassword());
        user.setRole(dto.getRole());

        return user;
    }
    /**
     * maps User entity to UserResponseDTO for sending in API response
    */
    public static UserResponseDTO toDTO(User user) {

        UserResponseDTO dto = new UserResponseDTO();
        dto.setId(user.getId());
        dto.setName(user.getName());
        dto.setEmail(user.getEmail());
        dto.setRole(user.getRole());

        return dto;
    }
}