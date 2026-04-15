package session1.oop;

public class GraduateStudent extends Student {

    // additional variable for specialization
    private String specialization;

    // constructor
    public GraduateStudent(String name, int rollNo, int marks, String specialization) {

        //super keyword is used to call the constructor of the parent class (Student) 
        // to initialize the inherited variables (name, rollNo, marks).
        super(name, rollNo, marks);
        this.specialization = specialization;
    }

    // method overriding (runtime polymorphism) 
    @Override
    public void display() {
        super.display();
        System.out.println("Specialization: " + specialization);
    }

    // method overloading (compile-time polymorphism)
    public void show(String s) {
        System.out.println("String value: " + s);
    }
}
