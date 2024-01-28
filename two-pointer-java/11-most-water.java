/*
 
    You are given an array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice you may not slant the container.


    EXAMPLE 1: 

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    

    EXAMPLE 2: 

    Input: height = [1,1]
    Output: 1


    Approach: 

    Initialize a maxArea of 0.
    Start with a pointer on each end of the array. The greater the distance between the two values indicies, the greater potential for a larger area.

    If the left pointer value is less then or equal to the right pointer value, calculate area as such:
        (j-1) * left; (the distance between the two values multiplied by the lower of the two) &
        increment left pointer
    else calculate area as such: 
        (j-1) * right; (the distance between the two values multiplied by the lower of the two) &
        decrement right pointer

    If the area calculated is greater than the maxArea, then update maxArea.

    Continue loop until the pointers meet each other
    

 */




import java.util.*;

class main {

    public static void main(String[] args) {

        System.out.println(maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));

    }



    public static int maxArea(int[] height) {
        int maxArea = 0;
        int i = 0, j = height.length - 1;

        while (i < j) {
            int area;
            int left = height[i];
            int right = height[j];
            if (left <= right) {
                area = (j-i) * left;
                i++;
            } else {
                area = (j-i) * right;
                j--;
            }
            if (area > maxArea) maxArea = area;
        }
        
        return maxArea;

    }
    
}
