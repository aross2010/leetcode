/*
 

    Given n non-negative intergers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Example 1: 

    Input: height = [0,1,0,2,1,01,3,2,1,2,1]
    output: 6


    Example 2: 

    Input: height = [4,2,0,3,2,5]
    Output: 9

 */



import java.util.*;

class main {

    public static void main(String[] args) {

        System.out.println(trap(new int[]{4,2,3}));

    }

    public static int trap(int[] height) {

        int trapped = 0;

        int left = 0, right = height.length - 1, leftMax = 0, rightMax = 0;

        while (left < right) {
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            trapped += leftMax < rightMax ? leftMax - height[left++] : rightMax - height[right--];
        }

        return trapped;
    }
    
}


