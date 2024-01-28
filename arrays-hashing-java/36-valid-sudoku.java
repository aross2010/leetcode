/*

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repitition
    2. Each column must contain the digits 1-9 without repitition
    3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repitition

Note:
    - A Sudoku board (partitally filled) could be valid but is not necessarily solvable
    - Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


    1. Each row must contain the digits 1-9 without repitition
    2. Each column must contain the digits 1-9 without repitition
    3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repitition


*/

/* 

APPROACH: 
** loop through the board and use string template literals and a set to keep track of board values in rows, cols, and boxes

- loop through 2D array

    if there is no value, ('.'), then continue to next cell

    create unique strings to add to set that contain its position (row, col or square) w/ the value

    if the set already contains an equivalent string, that means we have seen that value in already in the same row col or box -> return false
    else add all the strings to the set

- if made through loop return true

*/

import java.util.*;

class Main {

    public static boolean isValidSudoku(String[][] board) {

        Set<String> set = new HashSet<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                String value = board[i][j];
                if (value == ".") continue;
                String row = String.format("row: %d value: %d", i, value);
                String col = String.format("col: %d value: %d", i, value);
                String box = String.format("box: %d value: %d", Math.floor(i/3), Math.floor(j/3));
                if (set.contains(row) || set.contains(col) || set.contains(box)) return false;
                set.add(row);
                set.add(col);
                set.add(box);
            }
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(isValidSudoku(new String[][]{
            {"5", "3", ".", ".", "7", ".", ".", ".", "." },
            {"6", ".", ".", "1", "9", "5", ".", ".", "."},
            {".", "9", "8", ".", ".", ".", ".", "6", "."},
            {"8", ".", ".", ".", "6", ".", ".", ".", "3"},
            {"4", ".", ".", "8", ".", "3", ".", ".", "1"},
            {"7", ".", ".", ".", "2", ".", ".", ".", "6"},
            {".", "6", ".", ".", ".", ".", "2", "8", "."},
            {".", ".", ".", "4", "1", "9", ".", ".", "5"},
            {".", ".", ".", ".", "8", ".", ".", "7", "9"},
        }));
    }
    
}
