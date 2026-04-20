package com.todo.todo_app.dto;

import com.todo.todo_app.entity.Status;
import java.time.LocalDateTime;

// response dto (what we send back to client)
public class TodoResponseDTO {

    private Long id; //long as it is standard in spring data jpa for id
    private String title;
    private String description;
    private Status status;
    private LocalDateTime createdAt;

    public TodoResponseDTO() {}

    // getters and setters
    // created by ide to avoid boilerplate code
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }
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
    public void setStatus(Status status) {
        this.status = status;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }
    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
  
}