package session1.arrays;

import java.util.Scanner;

public class LinearSearch {

       // linear search function
    static int linearSearch(int[] arr, int n, int key) {

        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of  elements: ");
        int n = sc.nextInt();
       // declaring an array of n size
        int[] arr = new int[n];

        System.out.println("Enter  elements:");
        for (int i = 0; i < n; i++) {

            arr[i] = sc.nextInt();

        }

        System.out.print("Enter element to search: ");
        // taking key input from the user
        int key = sc.nextInt();
        // calling linear search function and if element is found it will return index otherwise -1
        int index = linearSearch(arr, n, key);

        if (index != -1) {
            System.out.println("Element found at index: " + index);
        } else {
            System.out.println("Element not found");
        }

        
    }

 
}