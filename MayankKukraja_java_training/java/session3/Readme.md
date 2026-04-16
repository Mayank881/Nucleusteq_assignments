# Spring Boot REST API – User Management

## Overview

This project is a Spring Boot REST API application that manages users using in-memory data. It follows a layered architecture (Controller → Service → Repository) and demonstrates core Spring concepts such as Dependency Injection, Inversion of Control (IoC), and RESTful API design.

The application allows searching, submitting, and deleting users with proper validation and exception handling.

---

## Technologies Used

* Java 17
* Spring Boot
* Maven
* Postman (for API testing)

---

## Project Structure

The project is organized using a layered architecture:

* **Controller**: Handles HTTP requests and responses
* **Service**: Contains business logic and validation
* **Repository**: Stores and manages in-memory user data
* **Model**: Defines the User entity
* **Exception**: Handles application-wide exceptions

Directory structure:

```
java/session3/
 ├── src/
 │   ├── main/java/com/mayank/session3/
 │   │   ├── controller/
 │   │   ├── service/
 │   │   ├── repository/
 │   │   ├── model/
 │   │   └── exception/
 │   └── resources/
 ├── pom.xml
 └── README.md
```

---

## Key Concepts Implemented

* Constructor-based Dependency Injection
* Inversion of Control (IoC)
* Component Scanning using annotations
* Layered Architecture
* REST API Design
* Input Validation
* Global Exception Handling

---

## API Endpoints

### 1. Search Users

**Endpoint:**
GET /users/search

**Query Parameters (all optional):**

* name (String, case-insensitive)
* age (Integer, exact match)
* role (String, case-insensitive)

**Examples:**

```
/users/search
/users/search?name=Priya
/users/search?age=30
/users/search?role=USER
/users/search?age=30&role=USER
```

**Behavior:**

* No parameters → returns all users
* With parameters → filters users based on conditions

---

### 2. Submit User

**Endpoint:**
POST /users/submit

**Request Body (JSON):**

```
{
  "name": "Mayank",
  "age": 22,
  "role": "USER"
}
```

**Responses:**

* 201 Created → User submitted successfully
* 400 Bad Request → Invalid input

**Validation Rules:**

* Name must not be null or empty
* Age must not be null
* Role must not be null or empty

---

### 3. Delete User

**Endpoint:**
DELETE /users/{id}?confirm=true

**Behavior:**

* If confirm=false or missing → user is not deleted
* If confirm=true → user is deleted

**Examples:**

```
DELETE /users/1
DELETE /users/1?confirm=true
```

---

## Exception Handling

The application uses a global exception handler to manage validation errors and return proper HTTP responses.

* CustomException is used for validation failures
* GlobalExceptionHandler returns HTTP 400 with error message

---

## Testing APIs

All APIs were tested using Postman.

Steps:

1. Open Postman
2. Select HTTP method (GET, POST, DELETE)
3. Enter the API URL
4. For POST requests, provide JSON body
5. Send request and verify response

---

## How to Run the Project

1. Navigate to the project directory:

```
java/session3
```

2. Run the application:

```
mvn spring-boot:run
```

3. Access APIs at:

```
http://localhost:8080
```

---

## Features

* In-memory user storage
* Dynamic filtering of users
* Input validation with proper error handling
* RESTful API design
* Clean and maintainable code structure

---

## Conclusion

This project demonstrates the implementation of a Spring Boot REST API with proper architecture, validation, and exception handling. It provides a clear understanding of backend development fundamentals and API design.
