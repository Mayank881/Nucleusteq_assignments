package com.mayank.session2.component;

import org.springframework.stereotype.Component;

// returns long message
@Component
public class LongMessageFormatter {

    public String format() {
        return "This is a long formatted message";
    }
}