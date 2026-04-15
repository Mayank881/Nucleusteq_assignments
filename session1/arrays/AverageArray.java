package session1.arrays;

import java.util.Scanner;

public class AverageArray {

    public static void main(String[] args) {

        // taking size input from the user
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");

        int n = sc.nextInt();
        //declaring a array of n size
        int[] arr = new int[n];

        // taking array input
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;

        // calculating sum
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }

        double average = (double) sum / n;

        System.out.println("Average is: " + average);

    
    }
}