package com.todo.todo_app.service;

import org.springframework.stereotype.Component;

// dummy service to simulate external notification 

@Component
public class NotificationServiceClient {

    public void sendNotification(String message) {

        System.out.println("Notification sent: " + message);
    }
}