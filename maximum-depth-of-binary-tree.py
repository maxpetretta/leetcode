from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Use DFS (recursion) to count depth of subtrees, O(n), O(n)
        # if root is None:
        #     return 0
        # left = 1 + self.maxDepth(root.left)
        # right = 1 + self.maxDepth(root.right)
        # return max(left, right)
        
        
        # Use BFS (iteration) to count depth of children, O(n), O(log n)
        stack = [[root, 1]]
        answer = 0

        while stack:
            node, depth = stack.pop()
            if node:
              answer = max(answer, depth)
              stack.append([node.left, depth + 1])
              stack.append([node.right, depth + 1])
        return answer
        

# Testcases
# [3,9,20,null,null,15,7]
# [1,null,2]
# [0,2,4,1,null,3,-1,5,1,null,6,null,8]
