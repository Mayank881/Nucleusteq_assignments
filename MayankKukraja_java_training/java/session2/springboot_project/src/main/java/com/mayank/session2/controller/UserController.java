package com.mayank.session2.controller;

import com.mayank.session2.model.User;
import com.mayank.session2.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// this class handles api requests 
// this is the entry point for clients to interact with our application 
// and it uses the service to perform operations and return responses
// @Restcontroller tells Spring that this class will handle http requests and return responses in json format
@RestController
public class UserController {

    private UserService service;

    // constructor injection to get the service instance from Spring
    public UserController(UserService service) {
        this.service = service;
    }

    // get all users 
    // @GetMapping("/users") means this method will handle GET requests to /users endpoint
    @GetMapping("/users")
    public List<User> getUsers() {
        return service.getAllUsers();
    }

    // get user by id
    @GetMapping("/users/{id}")
    // @PathVariable means the id in the url will be passed as a parameter to this method
    public User getUser(@PathVariable Long id) {
        return service.getUserById(id);
    }

    // create new user
    @PostMapping("/users")
    public String addUser(@RequestBody User user) {
        service.addUser(user);
        return "User added";
    }
}