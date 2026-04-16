package com.example.demo.component;

import org.springframework.stereotype.Component;

// This component handles notification logic
@Component
public class NotificationComponent {

    // Method to send notification
    public String sendNotification() {
        return "Notification sent";
    }
}