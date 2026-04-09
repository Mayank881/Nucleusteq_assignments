package session1.oop;

public class Student {

    // private variables  for acheiving encapsulation
    private String name;

    private int rollNo;
    private int marks;

    // constructor
    public Student(String name, int rollNo, int marks) {
        this.name = name;
        this.rollNo = rollNo;
        this.marks = marks;
    }

    // getters
    public String getName() {
        return name;
    }

    public int getRollNo() {
        return rollNo;
    }

    public int getMarks() {
        return marks;
    }

    // method to display details
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Marks: " + marks);
    }

    // method overloading example
    public void show(int a) {
        System.out.println("Integer value: " + a);
    }
}