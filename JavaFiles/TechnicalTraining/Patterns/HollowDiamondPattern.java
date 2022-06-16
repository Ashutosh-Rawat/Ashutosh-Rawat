import java.util.Scanner;

public class HollowDiamondPattern {
    private static void hollowDiamond(int size) {
        int i, j, diff;
        diff = size / 2;

        for (i = 1; i <= diff; i++) {
            System.out.print("\t");
            for (j = 1; j <= diff - i; j++) {
                System.out.print(" ");
            }
            if (i == 1) {
                System.out.print("*");
            } else {
                System.out.print("*");
                for (j = 1; j <= 2 *i - 3; j++) {
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.print("\n");
        }

        for (i = diff + 1; i < size; i++) {
            System.out.print("\t");
            for (j = 1; j <= i - diff; j++) {
                System.out.print(" ");
            }
            if (i == size - 1) {
                System.out.print("*");
            }
            else {
                System.out.print("*");
                for (j = 1; j <= 2 *(size - i) - 3; j++) {
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x;
        System.out.println("Enter size of diamond: ");
        x = in.nextInt();
        if (x % 2 == 1)
            x++;

        hollowDiamond(x);
    }
}