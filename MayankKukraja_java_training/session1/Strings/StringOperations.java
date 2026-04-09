/***********--- IN THIS SECTION I JUST CREATED ONE FILE INSTEAD OF THREE AND 
    ------------ CREATED DIFFERENT DIFFERENT METHODS FOR EACH QUESTION */

package session1.Strings;

import java.util.Scanner;
import java.util.Arrays;

public class StringOperations {


    // -------- Reverse String fucntion using --------
    static String reverseString(String str) {
        String rev = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            rev = rev + str.charAt(i);
        }

        return rev;
    }

    // -------- Count Vowels fucntion  --------
    static int countVowels(String str) {
        int count = 0;

        for (int i = 0; i < str.length(); i++) {
            // converting character to lowercase to handle both uppercase and lowercase vowels
            //character.toLowerCase() method is used to convert a character to lowercase. 
            // It takes a character as input and returns the lowercase equivalent of that character. 
            // If the input character is already in lowercase or is not an alphabetic character, 
            // it will return the character unchanged.
            char ch = Character.toLowerCase(str.charAt(i));

            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                count++;
            }
        }

        return count;
    }

    // -------- Anagram Check function --------
    static boolean isAnagram(String s1, String s2) {
        
        //regex "\\s" is used to match any whitespace character (spaces, tabs, etc.)
        //  and replaceAll() method is used to replace all occurrences of the matched 
        // whitespace characters with an empty string ("").
        s1 = s1.replaceAll("\\s", "").toLowerCase();
        s2 = s2.replaceAll("\\s", "").toLowerCase();

        if (s1.length() != s2.length()) {
            return false;
        }
       
        // character arrays arr1 and arr2 are created from the input strings s1 and s2 using the toCharArray() method.
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);
         //returns true of false based on whether the two sorted character arrays are equal.
        return Arrays.equals(arr1, arr2);

    }
    

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // input string FROM USER
        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        // reverse string called
        String reversed = reverseString(str);
        System.out.println("Reversed String: " + reversed);

        // count vowels called
        int count = countVowels(str);
        System.out.println("Number of vowels: " + count);

        // anagram check called
        System.out.print("Enter second string for anagram check: ");
        String str2 = sc.nextLine();
       

        // using the isAnagram method to check if the two strings are anagrams and printing the result
        if (isAnagram(str, str2)) {
            System.out.println("Strings are Anagrams");
        } else {
            System.out.println("Strings are NOT Anagrams");
        }
    }

    
}