package com.example.demo.service;

import com.example.demo.model.User;
import com.example.demo.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;

// This class contains business logic
@Service
public class UserService {

    private final UserRepository userRepository;

    // Constructor Injection (mandatory as per assignment)
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // Method to get all users
    public List<User> getAllUsers() {
        return userRepository.getAllUsers();
    }

    // Method to create a new user
    public void createUser(User user) {
        userRepository.addUser(user);
    }

    // Method to get user by id
    public User getUserById(int id) {
        return userRepository.getUserById(id);
    }
}