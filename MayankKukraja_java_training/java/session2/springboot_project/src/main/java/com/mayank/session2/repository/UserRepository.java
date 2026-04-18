package com.mayank.session2.repository;

import com.mayank.session2.model.User;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

// this class handles user data (in-memory)
// as we are not using a database, we will store users in a list
@Repository
public class UserRepository {

    // list to store users
    private List<User> users = new ArrayList<>();

    // adding some dummy users to the list when the repository is created
    public UserRepository() {
        users.add(new User(1L, "Aman"));
        users.add(new User(2L, "Riya"));
    }

    //it return all users 
    public List<User> getAllUsers() {
        return users;
    }

    // find user by id
    public User getUserById(Long id) {
        //uses a simple loop to find the user with the given id
        for (User user : users) {
            if (user.getId().equals(id)) {
                return user;
            }
        }
        return null;
    }

    // add new user to the list
    public void addUser(User user) {
        users.add(user);
    }
}