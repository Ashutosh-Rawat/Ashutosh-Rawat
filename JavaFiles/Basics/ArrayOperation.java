import java.util.*;
class arrayOperation {
    static Scanner sc = new Scanner(System.in);

    static int[] doubleVal(int[] Array) {
        for (int j = 0; j < 10; j++) {
            Array[j] = 2 * Array[j];
        }
        return Array;
    }
    static void dispElement(int[] arr) {
        for(int i=0;i<10;i++) {
            if(i==0) {
                System.out.print("[ ");
            }
            System.out.print(arr[i]);
            if(i<9) {
                System.out.print(", ");
            }
            if(i==9) {
                System.out.println(" ]");
            }
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] inputArray = new int[10];

        for(int i=0;i<10;i++) {
            System.out.print("Enter integer "+(i+1)+" ");
            inputArray[i] = sc.nextInt();
        }
        System.out.println("Array before doubleVal: ");
        dispElement(inputArray);
        doubleVal(inputArray);
        System.out.println("Array after doubleVal: ");
        dispElement(inputArray);
    }
}
