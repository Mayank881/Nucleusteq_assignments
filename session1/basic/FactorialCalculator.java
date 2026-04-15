package session1.basic;

import java.util.Scanner;

public class FactorialCalculator {

    public static void main(String[] args) {

        // taking input from user
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        
       //factorial of a number is the product of all positive integers less than or equal to that number,
       //  using int for factorial as it can hold larger values than short or byte which are less precise

        int factorial = 1;

        // loop from 1 to number to store the multiplication of all numbers from 1 to number in factorial variable
        for (int i = 1; i <= number; i++) {
            factorial = factorial * i;

        }

        System.out.println("Factorial is: " + factorial);

    
    }
}