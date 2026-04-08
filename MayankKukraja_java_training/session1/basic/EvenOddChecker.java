package session1.basic;

import java.util.Scanner;

public class EvenOddChecker {

    public static void main(String[] args) {

        // taking input from user
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        // checking even or odd using modulus operator
        if (number % 2 == 0) {
            System.out.println("Number is Even");
        } else {
            System.out.println("Number is Odd");

        }

    }
}