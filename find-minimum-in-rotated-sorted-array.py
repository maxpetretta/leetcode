from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force search, O(n), O(1)
        # minimum = float("inf")
        # for i in range(len(nums)):
        #     minimum = min(nums[i], minimum)
        # return minimum
    
        
        # Optimize binary search for rotation, O(log n), O(1)
        minimum = float("inf")
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(nums[left], minimum)
                break
            mid = (left + right) // 2
            minimum = min(nums[mid], minimum)
            
            if nums[left] <= nums[mid]:
                left = mid + 1      # Search right
            else:
                right = mid - 1     # Search left
        return minimum


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.findMin(nums=[3,4,5,1,2]))
    print(solver.findMin(nums=[4,5,6,7,0,1,2]))
    print(solver.findMin(nums=[11,13,15,17]))
    print(solver.findMin(nums=[1]))
    print(solver.findMin(nums=[2,3,4,5,1]))
