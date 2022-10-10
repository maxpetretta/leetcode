from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use DFS (recursion) to compare every node, O(n), O(n)        
        # if p is None and q is None:
        #     return True
        # elif p is None or q is None:
        #     return False
        # elif p.val != q.val:
        #     return False
        
        # return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        
    
        # Use BFS (iteration) to compare every node, O(n), O(n)
        queue = deque([(p, q)])
        
        while queue:
            p, q = queue.popleft()
            if p is None and q is None:
                continue
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False
            queue.append([p.left, q.left])
            queue.append([p.right, q.right])
        return True


# Testcases
# [1,2,3], [1,2,3]
# [1,2], [1,null,2]
# [1,2,1], [1,1,2]
