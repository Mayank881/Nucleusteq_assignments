package com.reimbursement.backend.service;

import com.reimbursement.backend.entity.User;
import com.reimbursement.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

// user related logic
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    /**
     * create new user
     */
    public User createUser(User user) {
        return userRepository.save(user);
    }

    /**
     * get all users
     */
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    /**
     * assign manager to employee
     */
    public User assignManager(Long employeeId, Long managerId) {

        User employee = userRepository.findById(employeeId).orElse(null);
        User manager = userRepository.findById(managerId).orElse(null);

        if (employee != null && manager != null) {
            employee.setManager(manager);
            return userRepository.save(employee);
        }

        return null;
    }
}