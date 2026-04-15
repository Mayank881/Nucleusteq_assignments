package session1.datatype;

public class OperatorsDemo {

    public static void main(String[] args) {

        int a = 10;
        int b = 5;

        // Arithmetic Operators
        //Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.
        System.out.println("Arithmetic Operators:");
        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));

        // Relational Operators
        //Relational operators are used to compare two values and return a boolean result (true or false). 
        System.out.println("\nRelational Operators:");
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));

        // Logical Operators
        //logical operators are used to combine multiple boolean expressions and return a boolean result.
        //  The main logical operators are AND (&&), OR (||), and NOT (!).
        System.out.println("\nLogical Operators:");
        System.out.println("(a > b && b > 0): " + (a > b && b > 0));
        System.out.println("(a < b || b > 0): " + (a < b || b > 0));
        System.out.println("!(a > b): " + !(a > b));
    }
}