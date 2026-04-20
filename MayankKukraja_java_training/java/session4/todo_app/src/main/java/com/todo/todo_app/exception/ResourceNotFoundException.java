package com.todo.todo_app.exception;

// custom exception when resource is not found
public class ResourceNotFoundException extends RuntimeException {

    public ResourceNotFoundException(String message) {
        super(message); // calling parent constructor to set the message
    }
}