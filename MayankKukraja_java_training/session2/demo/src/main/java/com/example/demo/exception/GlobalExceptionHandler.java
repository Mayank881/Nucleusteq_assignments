package com.example.demo.exception;

import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

// This class handles global exceptions
@RestControllerAdvice
public class GlobalExceptionHandler {

    // Handle all exceptions
    @ExceptionHandler(Exception.class)
    public String handleException(Exception e) {
        return "Error occurred: " + e.getMessage();
    }
}