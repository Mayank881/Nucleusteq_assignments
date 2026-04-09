package session1.oop;

public class MainTest {

    public static void main(String[] args) {

        // creating object 
        // passing values to constructor directly as i forgot to use setter methods in main class
        GraduateStudent student = new GraduateStudent("Mayank", 101, 85, "Computer Science");

        // calling display method (overriding)
        student.display();

        // calling polymorphism methods
        student.show(10);        // from parent class (Student)
        student.show("Hello");   // from child class   (GraduateStudent)
    }
}