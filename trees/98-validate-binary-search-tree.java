package trees;

/*
  Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 */


class Main {
    public static void main (String[] args) {
        TreeNode[] tree = new TreeNode[]{};


    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public boolean isValidBST(TreeNode root) {
        // use max and min to keep track of root vals to keep each node on correct side of tree
        // send the root as the max for left subtree, min for right subtree
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBST(TreeNode root, long min, long max) {

        if (root == null) return true;

        // if node on wrong side of tree
        if (root.val >= max || root.val <= min) return false;

        // check left and right children
        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
    }

    
}