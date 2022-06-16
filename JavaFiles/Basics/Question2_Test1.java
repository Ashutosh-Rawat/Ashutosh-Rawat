class Question2_Tes1 {

    public static int getSecondLargest(int[] a, int total) {
        int temp;
        for (int i = 0; i < total; i++) {
            for (int j = i + 1; j < total; j++) {
                if (a[i] > a[j]) {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
        return a[total-2];
    }
    public static void main(String args[]) {
        int array1[]={ 1,2,5,6,3,2, 9, 4, 15, 12 };
        int array2[]={ 22, 35, 54, 65, 63, 24, 29, 10, 8, 100, 43, 23, 1 };
        System.out.println("Second Largest element : "+getSecondLargest(array1, array1.length));
        System.out.println("Second Largest element : "+getSecondLargest(array2, array2.length));
    }
}
