package com.todo.todo_app.service;

import org.springframework.stereotype.Component;

// dummy notification service
@Component
public class NotificationServiceClient {

    public void sendNotification(String message) {
        System.out.println("Notification sent: " + message);
    }
}