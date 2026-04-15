package com.example.demo.service;

import com.example.demo.component.MessageFormatter;
import org.springframework.stereotype.Service;

import java.util.Map;

// This service decides which formatter to use at runtime
@Service
public class MessageService {

    private final Map<String, MessageFormatter> formatterMap;

    // Constructor Injection of all formatter components
    public MessageService(Map<String, MessageFormatter> formatterMap) {
        this.formatterMap = formatterMap;
    }

    // Method to return message based on type
    public String getMessage(String type) {

        // Get formatter based on type (shortFormatter / longFormatter)
        MessageFormatter formatter = formatterMap.get(type.toLowerCase() + "Formatter");

        if (formatter != null) {
            return formatter.formatMessage();
        }

        return "Invalid message type";
    }
}