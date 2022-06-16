/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ashutosh
 */
public class charOccurrence {
    static int countChar(String string, char character) {
        int count=0;
        for(int i=0;i<string.length();i++) {
            if(string.charAt(i)==character)
                count++;
        }
        return count;
    }
    public static void main(String[] args) {
        String string1 = "Two roads diverged in a yellow wood, " +"And sorry I could not travel both";
        char character1 = 't';
        System.out.println("count of character: "+countChar(string1,character1));
        char character2 = 'r';
        System.out.println("count of character: "+countChar(string1,character2));

    }
}
