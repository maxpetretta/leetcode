from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Build an inorder traversal list using recursion (DFS), return
        the k-1 element, O(n), O(n)
        """
        # def inorder(node):
        #     if not node:
        #         return []
        #     return inorder(node.left) + [node.val] + inorder(node.right)
        
        # return inorder(root)[k - 1]
        
        
        """
        Build an inorder traversal list using iteration (BFS), return
        the k-1 element, O(n), O(n)
        """
        # stack, inorder = [], []
        
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
                
        #     root = stack.pop()
        #     inorder.append(root.val)
        #     root = root.right
        # return inorder[k - 1]


        """
        Same as above, but stop after reaching the kth element
        O(h + k) where h = height of tree, O(h)
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root, k = stack.pop(), k - 1
            if not k:
                return root.val
            root = root.right


# Testcases
# [3,1,4,null,2], 1
# [5,3,6,2,4,null,null,1], 3
