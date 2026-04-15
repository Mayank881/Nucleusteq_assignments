package session2.demo.controller;

import session2.demo.model.User;
import session2.demo.service.UserService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

// this class handles all API requests
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    // constructor injection
    public UserController(UserService userService) {
        this.userService = userService;
    }

    // GET all users
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    // POST add user
    @PostMapping
    public String addUser(@RequestBody User user) {
        return userService.addUser(user);
    }

    // GET user by id
    @GetMapping("/{id}")
    public User getUserById(@PathVariable int id) {
        return userService.getUserById(id);
    }
}
