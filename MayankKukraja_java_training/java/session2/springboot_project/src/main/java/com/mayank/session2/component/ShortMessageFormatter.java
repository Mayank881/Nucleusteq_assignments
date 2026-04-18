package com.mayank.session2.component;

import org.springframework.stereotype.Component;

//it returns short message 

@Component
public class ShortMessageFormatter {

    public String format() {
        return "Short Message";
    }
}