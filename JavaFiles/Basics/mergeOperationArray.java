import java.util.Arrays;
import java.util.Scanner;
class mergeOperationArray {

    static int[] mergeArray(int[] arr1, int[] arr2) {     // this function is to merge two arrays
        int flag = 0;
        int length = arr1.length+arr2.length;
        int[] resultant_arr = new int[length];
        for(int k:arr1) {
            resultant_arr[flag] = k;
            flag++;
        }
        for(int l:arr2) {
            resultant_arr[flag] = l;
            flag++;
        }
        return resultant_arr;
    }
    static void showArray(int[] array) {
        int temp = 0;
            System.out.println(Arrays.toString(array));
        }

    public static void main(String[] args) {  // program inputs two arrays and merges them together printing them
        int number1, number2;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements for array 1: ");
        number1 = sc.nextInt();
        int[] Array1 = new int[number1];
        for(int i=0;i<Array1.length;i++) {
            System.out.print("Enter element "+(i+1)+": ");
            Array1[i] = sc.nextInt();
        }
        System.out.print("Enter number of elements in array 2: ");
        number2 = sc.nextInt();
        int[] Array2 = new int[number2];
        for(int j=0;j< Array2.length;j++) {
            System.out.print("Enter element "+(j+1)+": ");
            Array2[j] = sc.nextInt();
        }
        System.out.println("Input array 1: ");
        showArray(Array1);
        System.out.println("Input array 2: ");
        showArray(Array2);

        System.out.println("Merged array: ");
        showArray(mergeArray(Array1, Array2));
    }
}