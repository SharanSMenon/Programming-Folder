package com.sharans;

public class Main {

    public static void main(String[] args) {
        // Arrays
        double[] myFirstArray = new double[10];
        myFirstArray[5] = 50;
        System.out.println(myFirstArray[5]);
        int[] myIntArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        System.out.println(myIntArray[6]);
        double[] myDoubleArray = new double[10];
        for (int i = 0; i < 10; i++) {
            myDoubleArray[i] = i * 10;
        }
        System.out.println("---");
        for (int i = 0; i < 10; i++) {
            System.out.println(myDoubleArray[i]);
        }
        
    }
}