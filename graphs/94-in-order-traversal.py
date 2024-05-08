# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inOrder = []
        visited = set()
        stack = collections.deque()
        stack.append(root)
        current = root

        while stack and current != None:
            if current.left and current.left not in visited:
                stack.append(current.left)
                visited.add(current.left)
                current = current.left
            elif current.right and current.right not in visited:
                inOrder.append(stack.pop().val)
                stack.append(current.right)
                visited.add(current.right)
                current = current.right
            else:
                inOrder.append(stack.pop().val)
                if stack:
                    current = stack[-1]
            
        
        return inOrder

            

