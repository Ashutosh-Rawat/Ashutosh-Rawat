import java.util.*;
class arrayMethod {
  static Scanner sc = new Scanner(System.in);

  static void doubleValue(int[] Array) {
    for(int j=0;j<10;j++) {
      Array[j] = 2*Array[j];
    }
    System.out.println("Required array: ");
    for(int i=0;i<10;i++) {
      if(i==0) {
        System.out.print("[ ");
      }
      System.out.print(Array[i]);
      if(i<9) {
        System.out.print(", ");
      }
      if(i==9) {
        System.out.println(" ]");
      }
    }
    System.out.println();
  }

  static void displayElement(int[] Array) {
    System.out.print("Enter the number: ");
    int n = sc.nextInt();
    for(int k=0;k<10;k++) {
      if(Array[k] == n) {
        System.out.println("Your numbers before and after "+n+" are "+Array[k-1]+" and "+Array[k+1]);
        break;
      }
      else if (Array[k] != n && k==9) {
        System.out.println("Number is not present in array");
      }
    }
  }
  public static void main(String[] args) {
    int[] inputArray = new int[10];

    for(int i=0;i<10;i++) {
      System.out.print("Enter integer "+(i+1)+" ");
      inputArray[i] = sc.nextInt();
    }
    System.out.println("Array before doubleVale: ");
    displayElement(inputArray);
    doubleValue(inputArray);
    System.out.println("Array after doubleVal: ");
    displayElement(inputArray);
  }
}
