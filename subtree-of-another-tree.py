from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Compare the subRoot to the subtree at each node, O(n * m), O(n + m)
        if subRoot is None:
            return True
        elif root is None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# Testcases
# [3,4,5,1,2], [4,1,2]
# [3,4,5,1,2,null,null,null,null,0], [4,1,2]
