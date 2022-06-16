/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Ashutosh
 */

public class charCount {
    static void countOccurrence(String string) {
        int count[] = new int[200];
        int len = string.length();
        for(int i=0;i<len;i++)
            count[string.charAt(i)]++;
        
        char ch[] = new char[string.length()];
        for(int i=0;i<len;i++) {
            ch[i] = string.charAt(i);
            int iter = 0;
            for(int j=0;j<=i;j++) {
                if(string.charAt(i)==ch[j])
                    iter++;
            }
            if(iter==1)
                System.out.println("Number of occurence for "+string.charAt(i)+" : "+count[string.charAt(i)]);
        }
    }
    public static void main(String[] args) {
        String str = "Two roads diverged in a yellow wood, " +"And sorry I could not travel both";
        countOccurrence(str);
    }
}
