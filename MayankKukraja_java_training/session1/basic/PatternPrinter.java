package session1.basic;

import java.util.Scanner;

public class PatternPrinter {

    public static void main(String[] args) {

        // taking input for number of rows
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();

        // outer loop for rows
        for (int i = 1; i <= rows; i++) {

            // inner loop for printing stars
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            // move to next line after each row
            System.out.println();
        }

    }
}