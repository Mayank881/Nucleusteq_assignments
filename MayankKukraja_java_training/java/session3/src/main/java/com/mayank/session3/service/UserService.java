package com.mayank.session3.service;

import com.mayank.session3.model.User;
import com.mayank.session3.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {

    private UserRepository repository;

    // constructor injection (MANDATORY) - Spring will automatically inject the UserRepository bean here
    public UserService(UserRepository repository) {
        this.repository = repository;
    }

    // SEARCH USERS
    // This method allows searching for users based on optional criteria: name, age, and role.
    public List<User> searchUsers(String name, Integer age, String role) {

        List<User> allUsers = repository.getAllUsers();
        List<User> result = new ArrayList<>();
  
        // Iterate through all users and check if they match the provided criteria
        for (User user : allUsers) {

            boolean match = true;

            if (name != null && !user.getName().equalsIgnoreCase(name)) {
                match = false;
            }

            if (age != null && !user.getAge().equals(age)) {
                match = false;
            }

            if (role != null && !user.getRole().equalsIgnoreCase(role)) {
                match = false;
            }

            if (match) {
                result.add(user);
            }
        }

        return result;
    }

    // SUBMIT USER 
    
    public String submitUser(User user) {

        if (user.getName() == null || user.getName().trim().isEmpty()) {
            return "Invalid name";
        }

        if (user.getAge() == null) {
            return "Invalid age";
        }

        if (user.getRole() == null || user.getRole().trim().isEmpty()) {
            return "Invalid role";
        }

        return "User submitted successfully";
    }
    

    // DELETE USER
    public String deleteUser(Long id, boolean confirm) {

        if (!confirm) {
            return "Confirmation required";
        }

        repository.deleteUser(id);
        return "User deleted successfully";
    }
}