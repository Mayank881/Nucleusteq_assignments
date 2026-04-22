# Todo Application (Spring Boot)

## 📌 Overview

This is a Todo Application built using Spring Boot.
The project follows proper layered architecture and uses DTO to maintain clean API structure.

---

## 🚀 Features

* Create Todo
* Get all Todos
* Get Todo by ID
* Update Todo
* Delete Todo
* Input validation using @Valid
* Logging using SLF4J
* Notification simulation when a Todo is created
* Unit testing using JUnit and Mockito

---

## 🧱 Tech Stack

* Java 17
* Spring Boot
* Spring Data JPA
* H2 Database
* Maven
* JUnit & Mockito

---

## 📂 Project Structure

Controller → Service → Repository → Entity

DTO is used for:

* Request (TodoDTO)
* Response (TodoResponseDTO)

---

## 🔄 API Endpoints

### 1. Create Todo

POST /todos

### 2. Get All Todos

GET /todos

### 3. Get Todo by ID

GET /todos/{id}

### 4. Update Todo

PUT /todos/{id}

### 5. Delete Todo

DELETE /todos/{id}

---

## ⚙️ Key Concepts Used

* IoC (Spring manages objects)
* Dependency Injection (constructor-based)
* DTO mapping (manual)
* Exception handling
* Logging
* Unit testing

---

## 🔔 Notification Feature

A dummy service `NotificationServiceClient` is used.
Whenever a new Todo is created, a message is printed in console:

"Notification sent: New TODO created with id: X"

---

## 🧪 Testing

Unit tests are written for the Service layer using JUnit and Mockito.

Test cases include:

* Create Todo
* Get Todo
* Update Todo
* Delete Todo
* Exception scenarios
* Status validation

---

## 📌 Notes

* Status transitions allowed only:

  * PENDING → COMPLETED
  * COMPLETED → PENDING
* Invalid transitions throw error
* Entity is not exposed directly in APIs

---

## ▶️ How to Run

1. Clone the repository
2. Navigate to project folder

Run:

mvn spring-boot:run

3. Use Postman to test APIs

---

## 👨‍💻 Author

Mayank Kukraja
