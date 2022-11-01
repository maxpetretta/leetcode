import math
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        Take the first node as the root, and set all values less than a lower
        bound as the left subtree, and greater than upper as the right subtree
        O(n), O(n)
        """
        def subTree(lower, upper) -> Optional[TreeNode]:
            nonlocal index
            if index == length:
                return None
            
            value = preorder[index]
            if value < lower or value > upper:
                return None

            index += 1
            root = TreeNode(value)
            root.left = subTree(lower, value)
            root.right = subTree(value, upper)
            return root
        
        index, length = 0, len(preorder)
        return subTree(-math.inf, math.inf)


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.bstFromPreorder(preorder=[8,5,1,7,10,12]))
    print(solver.bstFromPreorder(preorder=[1,3]))
