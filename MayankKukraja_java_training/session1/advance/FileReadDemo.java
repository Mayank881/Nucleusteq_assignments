package session1.advance;

import java.io.File;
import java.util.Scanner;

public class FileReadDemo {

    public static void main(String[] args) {

        try {
            File file = new File("sample.txt");

            Scanner sc = new Scanner(file);
         // using hasNextLine() to check if there is another line in the file
         //  and nextLine() to read the line and print it until there are no more lines left in the file
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }

           

        } catch (Exception e) {
            System.out.println("Error reading file");
        }
    }
}