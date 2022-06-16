import java.lang.Math;
import java.util.Arrays;

class SquareRootArrayFunc {
    static void sqrt_method(int[] arr) {
        int max = arr[0];
        for(int i:arr) {
            if(max<i) max = i;
        }
        int number = (int) Math.sqrt(max);
        int[] int_array = new int[number+1];
        for(int k=0;k<= number;k++) {
            int_array[k] = k;
        }
        float[] sqrt_array = new float[arr.length];
        for(int t=0;t<sqrt_array.length;t++) {
            sqrt_array[t] = (float) Math.sqrt(arr[t]);
        }
        for(int j=0;j<sqrt_array.length;j++) {
            for(int x=0;x<int_array.length;x++) {
                if(sqrt_array[j]==(float)int_array[x]) {
                    System.out.println(arr[j]);
                }
            }

        }
    }
    public static void main(String[] args) {
        int[] Array = {21, 9, 2, 61, 16, 84, 81, 36, 89, 19, 91, 64, 14, 189, 169, 150, 121, 15, 100, 101};
        System.out.println("Input Array: ");
        System.out.println(Arrays.toString(Array));
        System.out.println("\nRequired numbers of array are: ");
        sqrt_method(Array);

    }
}