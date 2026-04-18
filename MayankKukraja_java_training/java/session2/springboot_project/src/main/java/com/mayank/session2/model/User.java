package com.mayank.session2.model;

// This class represents a user with an id and a name
public class User {

   
    private Long id;
    private String name;

    // default constructor to create user without id and name
    public User() {
    }

    // constructor to create user with id and name
    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    // returns user id
    public Long getId() {
        return id;
    }

    // returns user name
    public String getName() {
        return name;
    }

    // sets user id
    public void setId(Long id) {
        this.id = id;
    }

    // sets user name
    public void setName(String name) {
        this.name = name;
    }
}