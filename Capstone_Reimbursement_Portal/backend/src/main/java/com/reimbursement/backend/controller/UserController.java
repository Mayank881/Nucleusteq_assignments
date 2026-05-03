package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
import com.reimbursement.backend.dto.UserRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.service.UserService;
import com.reimbursement.backend.constants.Messages;

import jakarta.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;



/**
 * handles user APIs
 */
@CrossOrigin(origins = "*")
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
                                .body(new ApiResponse<>(true, Messages.USER_CREATED, user));
        }

        /**
         * get all users
         */
        @GetMapping
        public ResponseEntity<ApiResponse<Object>> getAllUsers(
                        @RequestParam(defaultValue = "0") int page,
                        @RequestParam(defaultValue = "5") int size) {

                return ResponseEntity.ok(
                                new ApiResponse<>(true, "Users fetched successfully",
                                                userService.getAllUsers(page, size)));
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
                                new ApiResponse<>(true, Messages.MANAGER_ASSIGNED, updatedUser));
        }

        /**
         * delete a user
         */
        @DeleteMapping("/{id}")
        public ResponseEntity<ApiResponse<String>> deleteUser(@PathVariable Long id) {

                userService.deleteUser(id);

                return ResponseEntity.ok(
                                new ApiResponse<>(true, Messages.USER_DELETED, null));
        }
}
