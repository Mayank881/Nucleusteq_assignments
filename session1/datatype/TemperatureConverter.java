package session1.datatype;

import java.util.Scanner;

public class TemperatureConverter {

    public static void main(String[] args) {

        // taking input from the user
        Scanner sc = new Scanner(System.in);

        System.out.println("Choose conversion:");

        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Fahrenheit to Celsius");
        
        int choice = sc.nextInt();
         // using nextInt() method to read the user's choice as an integer
        if (choice == 1) {
            System.out.print("Enter temperature in Celsius: ");
            double celsius = sc.nextDouble();
            //using double instead of float to allow for more precise temperature values, 

           //formula for converting Celsius to Fahrenheit is: F = (C * 9/5) + 32
            double fahrenheit = (celsius * 9 / 5) + 32;

            System.out.println("Temperature in Fahrenheit: " + fahrenheit);

        }
        else if (choice == 2) {
            System.out.print("Enter temperature in Fahrenheit: ");
            double fahrenheit = sc.nextDouble();
            
            //formula for converting Fahrenheit to Celsius is: C = (F - 32) * 5/9
            double celsius = (fahrenheit - 32) * 5 / 9;

            System.out.println("Temperature in Celsius: " + celsius);

        } 
        else {
            System.out.println("Invalid choice");
        }

    
    }
}