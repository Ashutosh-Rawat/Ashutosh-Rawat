/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 * @author Ashutosh
 *
 */
public class splitCase {
    static void split(String str) {
    	String[] result = str.split("(?<!(^|[A-Z]))(?=[A-Z])|(?<!^)(?=[A-Z][a-z])");
    	System.out.println("\nSplit Camel Case for string: "+str+" : ");
    	for(String s : result)
    		System.out.print("["+s+"], ");
    	System.out.println();
    }
    public static void main(String[] args) {
        //String str = "Two roads diverged in a yellow wood, " +"And sorry I could not travel both";
        String str1 = "CamelCase";
        String str2 = "camelCase";
        String str3 = "camelCASETHIS";
        String str4 = "CamelCASEthisONE";
    	split(str1);
    	split(str2);
    	split(str3);
    	split(str4);
    }
}
