import java.util.Scanner;
public class LeftPascalTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int number = sc.nextInt();
        for(int i=1;i<=number;i++) {
            for(int j=1;j<=number;j++) {
                if(j<=number-i)
                    System.out.print("  ");
                else
                    System.out.print("* ");
            }
            System.out.println();
        }
        for(int i=1;i<=number-1;i++) {
            for(int j=1;j<=number;j++) {
                if(j<=i)
                    System.out.print("  ");
                else
                    System.out.print("* ");
            }
            System.out.println();
        }
    }
}
