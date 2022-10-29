# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursively (DFS) search the tree for both p and q, returning the node
        where they are found in different subtrees, O(n), O(n)
        """
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root
        
        
        """
        Iteratively (BFS) search the tree for both p and q, returning the node
        where they are found in different subtrees, O(n), O(1)
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        

# Testcases
# [6,2,8,0,4,7,9,null,null,3,5], 2, 8
# [6,2,8,0,4,7,9,null,null,3,5], 2, 4
# [2,1], 2, 1
