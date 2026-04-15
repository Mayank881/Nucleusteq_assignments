package session1.arrays;

import java.util.*;

public class BubbleSort {

    public static void main(String[] args) {

        // taking input
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        // declaring an array of n size
        int[] arr = new int[n];

        System.out.println("Enter element:");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // bubble sort logic
        for (int i = 0; i < n - 1; i++) {

            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    // swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        // printing sorted array 
        System.out.println("Sorted array:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}