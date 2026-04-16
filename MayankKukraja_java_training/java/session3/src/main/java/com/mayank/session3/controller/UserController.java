package com.mayank.session3.controller;

import com.mayank.session3.model.User;
import com.mayank.session3.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    private UserService service;

    // constructor injection
    public UserController(UserService service) {
        this.service = service;
    }

    // SEARCH API
    // This API allows clients to search for users based on optional criteria: name, age, and role.
    @GetMapping("/search")
    public List<User> searchUsers(
            @RequestParam(required = false) String name,
            @RequestParam(required = false) Integer age,
            @RequestParam(required = false) String role) {

        return service.searchUsers(name, age, role);
    }

    // SUBMIT API
    // This API allows clients to submit a new user. The user data is sent in the request body as JSON.
    // 201 Created is returned on successful submission, while 400 Bad Request is returned if the input data is invalid.
    @PostMapping("/submit")
     public org.springframework.http.ResponseEntity<String> submitUser(@RequestBody User user) {

    String response = service.submitUser(user);

    if (response.startsWith("Invalid")) {
        return org.springframework.http.ResponseEntity.badRequest().body(response);
    }

    return org.springframework.http.ResponseEntity.status(201).body(response);
  }

    // DELETE API
    // This API allows clients to delete a user by their ID. A confirmation parameter is required.
    @DeleteMapping("/{id}")
    public String deleteUser(
            @PathVariable Long id,
            @RequestParam(required = false, defaultValue = "false") boolean confirm) {

        return service.deleteUser(id, confirm);
    }
}