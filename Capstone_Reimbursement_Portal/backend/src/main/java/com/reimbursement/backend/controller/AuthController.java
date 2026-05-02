package com.reimbursement.backend.controller;

import com.reimbursement.backend.dto.ApiResponse;
import com.reimbursement.backend.dto.LoginRequestDTO;
import com.reimbursement.backend.dto.UserResponseDTO;
import com.reimbursement.backend.service.UserService;

import jakarta.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import org.springframework.http.ResponseEntity;

@RestController
@RequestMapping("/auth")
@CrossOrigin(origins = "*")
public class AuthController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public ResponseEntity<ApiResponse<UserResponseDTO>> login(
            @Valid @RequestBody LoginRequestDTO request) {

        UserResponseDTO user = userService.login(request);

        return ResponseEntity.ok(
                new ApiResponse<>(true, "Login successful", user));
    }
}