package session2.demo.service;

import session2.demo.model.User;
import session2.demo.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;

// handles business logic
// controller should not directly talk to repository
@Service
public class UserService {

    private final UserRepository userRepository;

    // constructor injection (required)
    public UserService(UserRepository userRepository) {
        
        this.userRepository = userRepository;
    }

    // get all users
    public List<User> getAllUsers() {
        return userRepository.getAllUsers();

    }

    // add new user

    public String addUser(User user) {

        // basic validation
        if (user.getName() == null || user.getName().isEmpty()) {
            return "Name cannot be empty";

        }

        userRepository.addUser(user);
        return "User added successfully";

    }

    // get user by id
    public User getUserById(int id) {

        User user = userRepository.getUserById(id);

        if (user == null) {
            return null;
        }

        return user;
    }
}