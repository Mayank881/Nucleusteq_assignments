package com.example.demo.controller;

import com.example.demo.model.User;
import com.example.demo.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// This class handles all user-related API requests
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    // Constructor Injection
    public UserController(UserService userService) {
        this.userService = userService;
    }

    // API to get all users
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    // API to create a new user
    @PostMapping
    public String createUser(@RequestBody User user) {
        userService.createUser(user);
        return "User created successfully";
    }

    // API to get user by id
    @GetMapping("/{id}")
    public User getUserById(@PathVariable int id) {
        return userService.getUserById(id);
    }

    // Test API
    @GetMapping("/test")
    public String test() {
        return "Working";
    }

    // 🔥 ADD THIS METHOD HERE
    @GetMapping("/add")
    public String addUserFromBrowser() {
        User user = new User(1, "Mayank", "mayank@gmail.com");
        userService.createUser(user);
        return "User added from browser";
    }
}