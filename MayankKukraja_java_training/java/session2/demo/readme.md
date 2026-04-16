# Spring Boot Assignment - Session 2

## Overview

This project is a Spring Boot application implementing:

* User Management APIs
* Notification System
* Dynamic Message Formatter

## Features

### User APIs

* GET /users → Fetch all users
* POST /users → Create a user
* GET /users/{id} → Fetch user by ID

### Notification System

* GET /notify → Sends a notification

### Dynamic Message Formatter

* GET /message?type=short → Returns short message
* GET /message?type=long → Returns long message

## Concepts Used

* Spring Boot
* Layered Architecture (Controller → Service → Repository)
* Constructor-based Dependency Injection
* IoC (Inversion of Control)
* Component-based design
* Global Exception Handling

## Notes

* Uses in-memory data (no database)
* Clean and modular code structure
