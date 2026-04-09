package session1.advance;

/*
Interface:
Defines methods that must be implemented (100% abstraction)

Abstract Class:
Can have both abstract and concrete methods (partial abstraction)
*/

// interface with abstract method
interface Animal {
    void sound();
}

// abstract class with abstract and concrete method
abstract class Vehicle {
    abstract void start();

    void fuel() {
        System.out.println("Vehicle uses fuel");
    }
}

// class implementing both interface and abstract class
class Dog extends Vehicle implements Animal {

    public void sound() {
        System.out.println("Dog barks");
    }
 // implementing abstract method from Vehicle class
    void start() {
        System.out.println("Start method implemented");
    }
}

public class InterfaceAbstractDemo {

    public static void main(String[] args) {
      // creating object of Dog class
        Dog d = new Dog();

        d.sound();
        d.start();
        d.fuel();
    }
}