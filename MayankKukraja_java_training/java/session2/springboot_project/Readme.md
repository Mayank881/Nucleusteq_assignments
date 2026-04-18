# 🚀 User Management System (Spring Boot)

## 📌 Overview

This project is a Spring Boot based backend application developed as part of the Java Fundamentals assignment.
It implements a simple **User Management System**, along with **Notification System** and **Dynamic Message Formatter**.

Initially, I created the  project, but later I find some  flaws and weakpoints in it so i decided to  **updated and improved it by fixing structural issues, correcting mistakes, and properly implementing layered architecture** as per the assignment guidelines.

---

## ⚙️ Features

### 👤 1. User Management APIs

* **GET /users** → Fetch all users
* **GET /users/{id}** → Fetch user by ID
* **POST /users** → Add a new user

📌 Data is stored using **in-memory list (ArrayList)** (no database used).

---

### 🔔 2. Notification System

* **GET /notify** → Returns: `"Notification sent"`

✔ Implemented using `NotificationComponent`
✔ Demonstrates use of `@Component` and Dependency Injection

---

### 📨 3. Dynamic Message Formatter

* **GET /message?type=SHORT/LONG**

| Type  | Output                           |
| ----- | -------------------------------- |
| SHORT | Short Message                    |
| LONG  | This is a long formatted message |

✔ Uses:

* `ShortMessageFormatter`
* `LongMessageFormatter`

✔ Logic handled in **Service layer (not Controller)**

---

### ⚠️ 4. Exception Handling

* Custom Exception: `CustomException`
* Global Handler: `GlobalExceptionHandler`

Example:

* Invalid user → `"User not found"`

---

## 🏗️ Project Structure

```
controller  → handles API requests  
service     → contains business logic  
repository  → handles data (in-memory)  
component   → reusable logic (notification, formatter)  
model       → data classes  
exception   → error handling  
```

✔ Proper layered architecture
✔ Clean separation of concerns

---

## 🛠️ Technologies Used

* Java 17
* Spring Boot
* Maven
* REST APIs
* In-memory data storage

---

## 🧠 Concepts Implemented

* Dependency Injection (Constructor-based)
* Inversion of Control (IoC)
* Component Scanning
* Layered Architecture
* REST API Development
* Exception Handling

---

## ▶️ How to Run

1. Open project in VS Code / IntelliJ
2. Run:

```
./mvnw spring-boot:run
```

3. Server starts at:

```
http://localhost:8080
```

---

## 🧪 API Testing

### ✅ GET APIs (Browser)

```
http://localhost:8080/users
http://localhost:8080/users/1
http://localhost:8080/notify
http://localhost:8080/message?type=SHORT
```

---

### ➕ POST API (Use Postman / Thunder Client)

**POST /users**

📌 Body (JSON):

```
{
  "id": 3,
  "name": "Mayank"
}
```

✔ After adding user, verify:

```
GET /users
```

---

## 📝 Notes

* No database is used (as per assignment)
* Dummy data added for initial testing
* Project was improved after initial version to fix structure and follow proper design

---

## ✅ Conclusion

This project demonstrates core Spring Boot concepts with a clean and simple implementation.
Focus was on **correct structure, proper use of concepts, and working APIs**, rather than over-complicating the design.

---
