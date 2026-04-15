package session1.basic;

import java.util.*;

public class AreaCalculator {

    // using constant for PI so we don't hardcode it multiple times

    static final double PI = 3.14;
    // uses double for more precision instead of float which is less precise

    public static void main(String[] args) {

        // taking input from user
        Scanner scanner = new Scanner(System.in);

        // asking user which shape they want like circle, rectangle, triangle    
        System.out.println("Choose shape:");
        System.out.println("1. Circle");
        System.out.println("2. Rectangle");
        System.out.println("3. Triangle");

        int choice = scanner.nextInt();

        // based on choice, calling different methods
        switch (choice) {
            case 1:
                calculateCircle(scanner);
                break;

            case 2:
                calculateRectangle(scanner);
                break;

            case 3:
                calculateTriangle(scanner);
                break;

            default:
                System.out.println("Invalid choice");
        }

    }

    // method to calculate circle area

    public static void calculateCircle(Scanner scanner) {
        System.out.print("Enter radius: ");
        //using double for radius to allow for more precise input instead of int which is less precise
        double radius = scanner.nextDouble();

        double area = PI * radius * radius;

        System.out.println("Area of Circle: " + area);
    }

    // method to calculate rectangle area

    public static void calculateRectangle(Scanner scanner) {
        System.out.print("Enter length: ");

        double length = scanner.nextDouble();

        System.out.print("Enter width: ");

        double width = scanner.nextDouble();
        // calculating area using length and width, using double for more precision instead of int which is less precise
        double area = length * width;

        System.out.println("Area of Rectangle: " + area);
    }

    // method to calculate triangle area

    public static void calculateTriangle(Scanner scanner) {
        System.out.print("Enter base: ");

        double base = scanner.nextDouble();

        System.out.print("Enter height: ");
        double height = scanner.nextDouble();
        // calculating area using base and height, using double for more precision instead of int which is less precise
        double area = 0.5 * base * height;

        System.out.println("Area of Triangle: " + area);
    }
}
