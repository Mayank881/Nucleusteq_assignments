package com.example.demo.service;

import com.example.demo.component.NotificationComponent;
import org.springframework.stereotype.Service;

// This service handles notification flow
@Service
public class NotificationService {

    private final NotificationComponent notificationComponent;

    // Constructor Injection
    public NotificationService(NotificationComponent notificationComponent) {
        this.notificationComponent = notificationComponent;
    }

    // Method to trigger notification
    public String sendNotification() {
        return notificationComponent.sendNotification();
    }
}