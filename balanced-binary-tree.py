from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Top-down recursively compare the height of the left & right subtrees
        O(n log n), O(n)
        """
        # def height(root) -> int:
        #     if not root:
        #         return -1
        #     return 1 + max(height(root.left), height(root.right))
        
        # if not root:
        #     return True
        # elif abs(height(root.left) - height(root.right)) > 1:
        #     return False
        # else:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
        """
        Bottom-up recursively compare the height of the left & right subtrees
        O(n), O(n)
        """
        def height(root) -> tuple(bool, int):
            if not root: return (True, -1)
            
            left, right = height(root.left), height(root.right)
            if not left[0] or not right[0]:
                return (False, 0)
            return (abs(left[1] - right[1]) < 2, 1 + max(left[1], right[1]))
        
        return height(root)[0]


# Testcases
# [3,9,20,null,null,15,7]
# [1,2,2,3,3,null,null,4,4]
# []
