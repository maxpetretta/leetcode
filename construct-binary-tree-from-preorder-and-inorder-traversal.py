from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Recursively split the inorder array into left/right subtrees using
        the root from preorder, O(n), O(n)
        """
        # if not preorder or not inorder:
        #     return None
        
        # value = preorder[0]
        # root = TreeNode(value)
        # mid = inorder.index(value)
        
        # root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        # return root
        
    
        """
        Same as above, but use a hashmap to avoid repeated scans of inorder
        O(n), O(n)
        """
        def build(preorder, inorder) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None

            value = preorder[0]
            root = TreeNode(value)
            mid = indices[value]

            root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
            return root
        
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i
        
        return build(preorder, inorder)


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]))
    print(solver.buildTree(preorder=[-1], inorder=[-1]))
