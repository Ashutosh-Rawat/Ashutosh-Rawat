public class InvertedPyramid {
    public static void main(String[] args) {

        int height=5;
        int count = height;
        for(int i=1;i<=height;i++) {
            for(int j=0;j<=i-1;j++) {
                System.out.print("  ");
            }
            for(int k=1;k<=2*count-1;k++) {
                System.out.print("* ");
            }
            System.out.println();
            count--;
        }
    }
}  