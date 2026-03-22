# 📊 Student Performance Analyzer

## 📌 Overview
This project is a console-based JavaScript application that analyzes student performance using basic programming concepts like arrays, objects, loops, and functions.

The program calculates total marks, averages, subject-wise analysis, and determines grades based on performance and attendance.

---

## 🛠️ Technologies Used
- JavaScript (Core Concepts)
- Console (No DOM used)

---

## 📂 Project Structure
Mayank_frontend/
└── js/
└── mayank_student_analyzer.js---

## 🚀 How to Run the Program

### Using Node.js:
1. Open terminal
2. Navigate to project folder
3. Run:

node js/mayank_student_analyzer.js


### Using Browser Console:
1. Open browser (Chrome recommended)
2. Open Developer Tools → Console
3. Paste the code and run

---

## 📊 Features Implemented

### 1. Total Marks Calculation
Calculates total marks of each student by summing all subject scores.

---

### 2. Average Marks
Calculates average marks using total marks and number of subjects.

---

### 3. Subject-wise Highest Score
Finds the highest scorer in each subject across all students.

---

### 4. Subject-wise Average
Calculates average marks for each subject.

---

### 5. Class Topper
Identifies the student with the highest total marks.

---

### 6. Grade System
Grades are assigned based on average marks:

| Average Marks | Grade |
|--------------|------|
| 85+          | A    |
| 70–84        | B    |
| 50–69        | C    |
| Below 50     | Fail |

### Additional Fail Conditions:
- Any subject score ≤ 40 → Fail  
- Attendance < 75% → Fail  

---

## 📸 Output Screenshots

### 🔹 Total Marks Output
![Total Marks](/js/Screenshots/total.png)

### 🔹 Average Marks Output
![Average](/js/Screenshots/Average.png)

### 🔹 Subject-wise Highest
![subject-wise_highest](/js/Screenshots/highest.png)

### 🔹 Subject-wise Average
![subject-wise_avg](/js/Screenshots/Subject_average.png)

### 🔹 Class Topper
![Topper](/js/Screenshots/Topper.png)

### 🔹 Grade Output
![grades](/js/Screenshots/Grades.png)

---

## 🧠 Approach

- I used an array of objects to represent student data.
- Loops were used to iterate through students and subjects.
- Functions were created for each calculation to keep the code clean and reusable.
- Conditions were used to implement grading and fail logic.
- I avoided using DOM as per the assignment requirement and used only console output.

---

## 📌 Conclusion

This project helped me understand how to work with real-world data structures in JavaScript and how to break down a problem into smaller logical steps.

It also improved my understanding of loops, functions, and condition handling.

---

## 👨‍💻 Author
**Mayank Kukraja**