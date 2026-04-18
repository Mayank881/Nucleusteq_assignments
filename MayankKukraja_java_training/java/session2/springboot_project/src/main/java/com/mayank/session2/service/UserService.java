package com.mayank.session2.service;

import com.mayank.session2.model.User;
import com.mayank.session2.repository.UserRepository;
import org.springframework.stereotype.Service;
//adding import for notification component
import com.mayank.session2.component.NotificationComponent;
import java.util.List;

// this class contains business logic - like this is the brain of the application
// it acts as a bridge between the controller and the repository
// it uses the repository to get data and perform operations on it
//@Service annotation tells Spring that this class is a service component
@Service
public class UserService {

    private UserRepository repository;
    // adding notification component to the service
    private NotificationComponent notification;


    // constructor injection to get the repository instance from Spring
    // we also inject the notification component to use it in our service 
    public UserService(UserRepository repository, NotificationComponent notification) {
        this.repository = repository;
        this.notification = notification;
    }

    // get all users 
    public List<User> getAllUsers() {
        return repository.getAllUsers();
    }

    // get user by id
    public User getUserById(Long id) {
        return repository.getUserById(id);
    }

    // add new user
    public void addUser(User user) {
        repository.addUser(user);
    }
    // trigger notification
    //  a method to send notification using the notification component
    public String sendNotification() {
    return notification.sendNotification();
    }
}