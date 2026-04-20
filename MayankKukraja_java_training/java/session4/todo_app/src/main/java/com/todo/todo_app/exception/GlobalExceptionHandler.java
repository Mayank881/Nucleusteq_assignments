package com.todo.todo_app.exception;

import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

// handles all exceptions globally
//here @RestControllerAdvice is used to handle exceptions globally across the whole application
@RestControllerAdvice
public class GlobalExceptionHandler {
     
    // HANDLING RESOURCE NOT FOUND EXCEPTION
    @ExceptionHandler(ResourceNotFoundException.class)
    public String handleNotFound(ResourceNotFoundException ex) {
        return ex.getMessage();
    }
}