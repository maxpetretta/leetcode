from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use DFS (recursion) to swap left/right subtrees, O(n), O(n)
        # if root is None:
        #     return None
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left, root.right = right, left
        # return root
    
        
        # Use BFS (iteration) to swap left/right children, O(n), O(n)
        if root is None:
            return None
        
        queue = deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return root


# Testcases
# [4,2,7,1,3,6,9]
# [2,1,3]
# [1,2]
# []
