package session1.control;

public class SumEvenNumbers {

    public static void main(String[] args) {

        int i = 1;
        int sum = 0;

        // using while loop 
        while (i <= 10) {

            if (i % 2 == 0) {
                sum = sum + i;
            }

            i++;
        }

        System.out.println("Sum of even numbers from 1 to 10 is: " + sum);
    }
}