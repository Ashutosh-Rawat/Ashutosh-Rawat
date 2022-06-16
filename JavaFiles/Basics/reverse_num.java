import java.util.Scanner;
interface InfaceX {
    static void reverse(int num) {
        String num_in_str = String.valueOf(num);
        for(int i=(num_in_str.length()-1);i>=0;i--) {
            System.out.print(num_in_str.charAt(i));
        }
    }
}
public class reverse_num implements InfaceX {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int input_number = sc.nextInt();
        InfaceX.reverse(input_number);
    }
}
