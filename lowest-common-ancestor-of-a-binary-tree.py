# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursively search the tree for p & q.  Set a flag (mid) when one value
        is found.  Backtrack until both values are found, and return that node
        O(n), O(n)
        """        
        # if not root:
        #     return False

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # mid = (root == p or root == q)

        # if (left + right + mid) > 1:
        #     return root
        # return (left or right or mid)
        
    
        """
        Iteratively search the tree for p & q.  Keep pointers to the parent of
        each node.  Once p & q are found, compare both sets of parents, and
        return the first common node, O(n), O(n)
        """
        stack = [root]
        parents = {root: None}
        
        # Build the dictionary of parent nodes
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        # Find the lowest common ancestor
        common = set()
        while p:
            common.add(p)
            p = parents[p]
        while q not in common:
            q = parents[q]
        return q


# Testcases
# [3,5,1,6,2,0,8,null,null,7,4], 5, 1
# [3,5,1,6,2,0,8,null,null,7,4], 5, 4
# [1,2], 1, 2
