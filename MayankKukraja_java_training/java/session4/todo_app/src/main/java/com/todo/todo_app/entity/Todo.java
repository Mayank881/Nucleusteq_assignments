package com.todo.todo_app.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;


//@entity annotation mapped the class to a database table named "todos"
@Entity
@Table(name = "todos")
public class Todo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)  // it auto generates the primary key value
    private Long id;

    @Column(nullable = false) //indicaete that the tittle column can't be null

    private String title;

    private String description;
     
    //@enumerated specify that status field stored as a sting in the database
    @Enumerated(EnumType.STRING) 
    private Status status;

    private LocalDateTime createdAt;

    public Todo() {}

    // Parameterized constructor 
    public Todo(Long id, String title, String description, Status status, LocalDateTime createdAt) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.status = status;
        this.createdAt = createdAt;
    }

    //now Getters and Setters 

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