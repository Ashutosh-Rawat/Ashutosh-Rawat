// this code prints the right pascal's triangle
import java.util.Scanner;
public class RightPascalTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number : ");
        int number = sc.nextInt();
        int counter = 0;

        for(int i=1;i<=number;i++) {
            for(int j=1;j<=i;j++)
                System.out.print("*  ");
            System.out.println();
        }
        for(int i=1;i<=number-1;i++) {
            for(int j=1;j<=number-i;j++)
                System.out.print("*  ");
            System.out.println();
        }
    }
}
