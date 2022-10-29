import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Using recursion (DFS), check if each node falls within the low/high
        range for the subtree, O(n), O(n)
        """
        # def validate(node, low, high) -> bool:
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= high:
        #         return False
        #     return (validate(node.left, low, node.val) and
        #             validate(node.right, node.val, high))
        
        # low, high = -math.inf, math.inf
        # return validate(root, low, high)


        """
        Using iteration (BFS), check if each node falls within the low/high
        range for the subtree, O(n), O(1)
        """
        # if not root:
        #     return True
        
        # stack = [(root, -math.inf, math.inf)]
        # while stack:
        #     node, low, high = stack.pop()
        #     if not node:
        #         continue
        #     if node.val <= low or node.val >= high:
        #         return False
        #     stack.append((node.left, low, node.val))
        #     stack.append((node.right, node.val, high))
        # return True
        
        
        # Search the tree using inorder traversal, O(n), O(n)
        prev, stack = -math.inf, []
        
        while stack or root:
            # Add all left nodes to stack
            while root:
                stack.append(root)
                root = root.left
            
            # Check each node inorder
            root = stack.pop()
            if root.val <= prev:
                return False
            prev, root = root.val, root.right
        return True


# Testcases
# [2,1,3]
# [5,1,4,null,null,3,6]
# [5,4,6,null,null,3,7]
