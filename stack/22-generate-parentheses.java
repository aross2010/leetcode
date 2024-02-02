package stack;

/*
 
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Input: n = 1
    Output: ["()"]

    Approach: 
    
    Build a recursuve tree of all possible combinations.

    start with empty string

    backtrack: 

        if there are less open parentheses than n, add an open parenthesis and backtrack into function
        if there are more open parentheses than closes, add a closed parenthesis and backtrack into function
        if the length of the string reaches 2n, the string has reached its limit of parentheses, add to combos (return) list

 */

import java.util.*;

class Main {

    public static List<String> generateParenthesis(int n) {
        List<String> combos = new ArrayList<>();
        backtrack(combos, "", 0, 0, n);
        return combos;
    }

    public static void backtrack(List<String> list, String str, int open, int close, int n) {

        // string contains all possible parentheses
        if (str.length() == n*2) {
            list.add(str);
            return;
        }

        if (open < n) 
            backtrack(list, str+"(", open+1, close, n);

        if (close < open) 
            backtrack(list, str+")", open, close+1, n);
        

    }
    
}
