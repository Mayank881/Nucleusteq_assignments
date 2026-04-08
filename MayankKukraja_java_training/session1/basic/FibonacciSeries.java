package session1.basic;

import java.util.Scanner;

public class FibonacciSeries {

    public static void main(String[] args) {

        // taking input from user
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number : ");

        int n = sc.nextInt();

        // first two numbers of series are always 0 and  1 
        int a = 0, b = 1;

        System.out.println("Fibonacci Series:");
         //fibonacci series is a series of numbers where each number is the sum of the two preceding ones,
         //  usually starting with 0 and 1.
        // printing series
        for (int i = 1; i <= n; i++) {
            System.out.print(a + " ");

            int next = a + b; // next term
            a = b;
            b = next;
        }
    }
}