package com.mayank.session2.service;

import com.mayank.session2.model.User;
import com.mayank.session2.repository.UserRepository;
import org.springframework.stereotype.Service;
//adding import for notification component, short message formatter and long message formatter
import com.mayank.session2.component.NotificationComponent;
import com.mayank.session2.component.ShortMessageFormatter;
import com.mayank.session2.component.LongMessageFormatter;
import java.util.List;

// this class contains business logic - like this is the brain of the application
// it acts as a bridge between the controller and the repository
// it uses the repository to get data and perform operations on it
//@Service annotation tells Spring that this class is a service component
@Service
public class UserService {

    private UserRepository repository;
    // adding notification component to the service, and also adding short and long
    // message formatters
    // to use them in our service methods
    private NotificationComponent notification;
    private ShortMessageFormatter shortFormatter;
    private LongMessageFormatter longFormatter;

    // constructor injection to get the repository instance from Spring
    // we are updating our constructor to also get the notification component and
    // message formatters from Spring
    // this is going to be a little bit messy here .

    public UserService(UserRepository repository,
            NotificationComponent notification,
            ShortMessageFormatter shortFormatter,
            LongMessageFormatter longFormatter) {
        this.repository = repository;
        this.notification = notification;
        this.shortFormatter = shortFormatter;
        this.longFormatter = longFormatter;
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
    // a method to send notification using the notification component
    public String sendNotification() {
        return notification.sendNotification();
    }

    //it return message based on type from the formatters  
    public String getMessage(String type) {

        if ("SHORT".equalsIgnoreCase(type)) {
            return shortFormatter.format();
        } else {
            return longFormatter.format();
        }
    }
}