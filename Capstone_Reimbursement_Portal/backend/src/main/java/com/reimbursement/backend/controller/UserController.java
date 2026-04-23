package com.reimbursement.backend.controller;

import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// handles user APIs
@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * create a new user
     */
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }

    /**
     * get all users
     */
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    /**
     * assign manager to employee
     */
    @PutMapping("/{employeeId}/assign/{managerId}")
    public User assignManager(@PathVariable Long employeeId,
                              @PathVariable Long managerId) {

        return userService.assignManager(employeeId, managerId);
    }
}