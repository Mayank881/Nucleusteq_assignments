package session1.advance;

public class ExceptionDemo {

    public static void main(String[] args) {
 // trying to divide a number by zero which will throw an ArithmeticException
        try {
            int a = 10;
            int b = 0;

            int result = a / b;

            System.out.println(result);

        }
        // catching the ArithmeticException and printing an error message
        catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero");

        }
        // using finally block to print a message indicating that the execution is completed 
        finally {
            System.out.println("Execution completed");
        }
    }
}