from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Find the midpoint of the array, and set it to the root node
        Recursively create the left/right subtrees from either side of the midpoint
        O(n), O(log n) since tree is height-balanced
        """
        if not nums: return None
        
        mid = len(nums) // 2 # Always picks left-middle node
        value = nums[mid]
        root = TreeNode(value)
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.sortedArrayToBST(nums=[-10,-3,0,5,9]))
    print(solver.sortedArrayToBST(nums=[1,3]))
