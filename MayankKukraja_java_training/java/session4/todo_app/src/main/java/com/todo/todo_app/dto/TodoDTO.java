package com.todo.todo_app.dto;

import com.todo.todo_app.entity.Status;
import jakarta.validation.constraints.NotNull; // validation annotation to ensure title is not null
import jakarta.validation.constraints.Size;    //to ensure title has a minimum length of 3 characters

// TodoDTO transfers data between client and server
public class TodoDTO {

    @NotNull
    @Size(min = 3)
    private String title;

    private String description;

    private Status status;

    // Constructor
    public TodoDTO() {}

    // Getters and Setters

    public String getTitle() {
        return title;
    }
    // setter for title
    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {

        return description;
    }

    public void setDescription(String description) { 

        this.description = description;
    }

    public Status getStatus() {     

        return status;
    }
   //  setter for status
    public void setStatus(Status  status) {    
        this.status = status;       
    }
}