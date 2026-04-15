package com.example.demo.component;

import org.springframework.stereotype.Component;

// This class provides short message format
@Component("shortFormatter")
public class ShortMessageFormatter implements MessageFormatter {

    // Implementation of formatMessage method
    @Override
    public String formatMessage() {
        return "Short Message";
    }
}