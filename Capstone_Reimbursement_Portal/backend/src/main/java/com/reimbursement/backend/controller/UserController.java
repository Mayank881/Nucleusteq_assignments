package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.service.UserService;

import jakarta.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;

import java.util.List;

/**
 * handles user APIs
 */
@CrossOrigin(origins = {
        "http://localhost:5500",
        "http://127.0.0.1:5500"
})
@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * create a new user
     */
    @PostMapping
    public ResponseEntity<ApiResponse<UserResponseDTO>> createUser(
            @Valid @RequestBody UserRequestDTO requestDTO) {

        UserResponseDTO user = userService.createUser(requestDTO);

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new ApiResponse<>(true, "User created successfully", user));
    }

    /**
     * get all users
     */
    @GetMapping
    public ResponseEntity<ApiResponse<List<UserResponseDTO>>> getAllUsers() {

        List<UserResponseDTO> users = userService.getAllUsers();

        return ResponseEntity.ok(
                new ApiResponse<>(true, "Users fetched successfully", users)
        );
    }

    /**
     * assign manager to employee
     */
    @PutMapping("/{employeeId}/assign/{managerId}")
    public ResponseEntity<ApiResponse<UserResponseDTO>> assignManager(
            @PathVariable Long employeeId,
            @PathVariable Long managerId) {

        UserResponseDTO updatedUser = userService.assignManager(employeeId, managerId);

        return ResponseEntity.ok(
                new ApiResponse<>(true, "Manager assigned successfully", updatedUser)
        );
    }
}

