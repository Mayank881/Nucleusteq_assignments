package session2.demo.repository;

import session2.demo.model.User;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

// this class will act like a database
// for now we are just storing data in memory (ArrayList)
@Repository
public class UserRepository {

    // list to store users
    private List<User> users = new ArrayList<>();

    // method to get all users
    public List<User> getAllUsers() {
        
        return users;
    }

    // method to add new user
    public void addUser(User user) {
        users.add(user);
    }

    // method to find user by id

    public User getUserById(int id) {

        // simple loop to find user
        for (User user : users) {
            if (user.getId() == id) {
                return user;
            }
        }


        // if not found return null
        return null;
    }
}