package com.example.demo.repository;

import com.example.demo.model.User;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

// This class acts as a data layer (in-memory storage)
@Repository
public class UserRepository {

    // Dummy list to store users
    private List<User> userList = new ArrayList<>();

    // Method to get all users
    public List<User> getAllUsers() {
        return userList;
    }

    // Method to add a new user
    public void addUser(User user) {
        userList.add(user);
    }

    // Method to get user by id
    public User getUserById(int id) {
        for (User user : userList) {
            if (user.getId() == id) {
                return user;
            }
        }
        return null; // return null if user not found
    }
}