from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Recursively place the new node at the first valid position in the BST
        average O(log n) worst case O(n), average O(log n) worst case O(n)
        """
        # if not root:
        #     return TreeNode(val)
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
        
    
        """
        Iteratively place the node at the first valid position in the BST
        average O(log n) worst case O(n), O(1)
        """
        if not root:
            return TreeNode(val)
        
        node = root
        while node:
            # Left subtree
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            # Right subtree
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right


# Testcases
# [4,2,7,1,3], 5
# [40,20,60,10,30,50,70], 25
# [4,2,7,1,3,null,null,null,null,null,null], 5
