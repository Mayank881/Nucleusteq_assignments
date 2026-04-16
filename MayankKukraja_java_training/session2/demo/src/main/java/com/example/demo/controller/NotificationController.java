package com.example.demo.controller;

import com.example.demo.service.NotificationService;
import org.springframework.web.bind.annotation.*;

// This controller handles notification API
@RestController
@RequestMapping("/notify")
public class NotificationController {

    private final NotificationService notificationService;

    // Constructor Injection
    public NotificationController(NotificationService notificationService) {
        this.notificationService = notificationService;
    }

    // API to trigger notification
    // GET /notify
    @GetMapping
    public String sendNotification() {
        return notificationService.sendNotification();
    }
}