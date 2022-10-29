from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Traverse the tree with DFS, adding the value of each node to
        the current level's list, O(n), O(n)
        """
        # def traverseList(node, level):
        #     if len(answer) == level:
        #         answer.append([])
            
        #     answer[level].append(node.val)
        #     if node.left:
        #         traverseList(node.left, level + 1)
        #     if node.right:
        #         traverseList(node.right, level + 1)
        
        # answer = []
        # traverseList(root, 0) if root else None
        # return answer


        """
        Traverse the tree with BFS, adding each node to a queue
        Pop from the queue and append the value to the current level's list
        Add any children back into the queue, O(n), O(n)
        """
        level, answer = 0, []
        queue = deque([root]) if root else None
        
        while queue:
            answer.append([])
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                answer[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return answer
        

# Testcases
# [3,9,20,null,null,15,7]
# [1]
# []
