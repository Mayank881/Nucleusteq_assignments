
package com.reimbursement.backend.controller;

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
    public UserResponseDTO createUser(@Valid @RequestBody UserRequestDTO requestDTO) {
        return userService.createUser(requestDTO);
    }

    /**
     * get all users
     */
    @GetMapping
    public List<UserResponseDTO> getAllUsers() {
        return userService.getAllUsers();
    }

    /**
     * assign manager to employee
     */
    @PutMapping("/{employeeId}/assign/{managerId}")
    public UserResponseDTO assignManager(@PathVariable Long employeeId,
                                         @PathVariable Long managerId) {
        return userService.assignManager(employeeId, managerId);
    }
}