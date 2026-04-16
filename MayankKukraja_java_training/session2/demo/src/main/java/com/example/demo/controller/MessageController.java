package com.example.demo.controller;

import com.example.demo.service.MessageService;
import org.springframework.web.bind.annotation.*;

// This controller handles dynamic message API
@RestController
@RequestMapping("/message")
public class MessageController {

    private final MessageService messageService;

    // Constructor Injection
    public MessageController(MessageService messageService) {
        this.messageService = messageService;
    }

    // API to get message based on type
    // GET /message?type=short OR long
    @GetMapping
    public String getMessage(@RequestParam String type) {
        return messageService.getMessage(type);
    }
}