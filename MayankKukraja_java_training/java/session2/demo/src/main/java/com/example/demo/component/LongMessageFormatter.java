package com.example.demo.component;

import org.springframework.stereotype.Component;

// This class provides long message format
@Component("longFormatter")
public class LongMessageFormatter implements MessageFormatter {

    // Implementation of formatMessage method
    @Override
    public String formatMessage() {
        return "This is a long formatted message";
    }
}