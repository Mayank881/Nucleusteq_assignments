package com.mayank.session2.exception;

import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

// handles all exceptions globally
// @restcontrolleradvice is  used to handle exceptions globally across the whole application.

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(CustomException.class)
    public String handleCustomException(CustomException ex) {
        return ex.getMessage();
    }
}