package stack;

/*
 
    Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.

    An input string is valid if: 

        1. Open brackets must be closed by the same type of brackets
        2. Open brackets must be closed in the correct order
        3. Every cllose breacket has a corresponding open bracket of the same type

    
    Input: "([]{})"
    Output: true

    Input: "({}"
    Output: false

    Approach: 

    Keep a stack of characters. Loop through the string. When encountering an open parentheses, push it to the stack.

    When encountering a closed parentheses, check the stack for a couple things: 
        1. if the stack is empty, that means this closes parenthese does not have an opening parenthese, return false
        2. if you pop the stack and the opening parenthese does not match the closing one, return false

    Finally, if the stack still contains characters, that means the opening parentheses in the stack never got a corresponding closing parenthese. Return false.

    Time: O(n) 
 */

import java.util.*;

class main {


    public static void main(String[] args) {
        System.out.println(isValid("([]{})"));
    }

    static boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        if (s.length() % 2 != 0) return false;

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') 
                stack.push(s.charAt(i));
            else {
                if (stack.isEmpty()) return false;
                char openingBracket = stack.pop();
                if ((c == ')' && openingBracket != '(') || (c == '}' && openingBracket != '{') || (c == ']' && openingBracket != '['))
                return false;
            }
        }

        if (!stack.isEmpty()) return false;

       
        


        return true;
    }

}
