package session1.control;

import java.util.Scanner;

public class MultiplicationTable {

    public static void main(String[] args) {

        // taking input
        Scanner sc = new  Scanner(System.in);

        System.out.print("Enter a number: " );
        int num = sc.nextInt();

        // printing table
        for (int i = 1; i <= 10; i++) {
            System.out.println(num +   " x " +  i + " = "  + (num * i));
        }
    }
}