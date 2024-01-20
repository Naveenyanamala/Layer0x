// Task 1

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


class Challenge {
    private static long  maxSubarray(int[] array) {
        int n= array.length;
        long max = Integer.MIN_VALUE, sum=0;
        for(int i=0;i<n; i++){
            sum+=array[i];
            max=Math.max(sum,max);
            if(sum<0){
                sum=0;
            }
        }
        return max;
    }

    public static void main(String[] args) {
       
        Scanner input = new Scanner(System.in);
        System.out.println("Enter no of test cases");
        int t = input.nextInt();
        while (t-- >0) {
            System.out.println("Enter size of array");
            int n= input.nextInt();
            int[] array = new int[n];
            System.out.println("Enter the array values");
            for(int i=0; i<n;i++){
                array[i]= input.nextInt();
            } 
            System.out.println("Maximum subArrays sum is: "+ maxSubarray(array));
        }
    }
}