from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force, O(n)
        # length = len(nums)
        # minimum = nums[0]
        # for i in range(1, length):
        #     minimum = min(nums[i], minimum)
        # return minimum
    
        
        # Binary search, O(log n)
        def binSearch(nums, start, end):
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[start]:
                return binSearch(nums, mid + 1, end)
            else:
                return binSearch(nums, start, mid - 1)
        
        if len(nums) == 1:
            return nums[0]
        elif nums[0] < nums[-1]:
            return nums[0]
        else:
            return binSearch(nums, 0, len(nums) - 1)


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.findMin(nums=[3,4,5,1,2]))
    print(solver.findMin(nums=[4,5,6,7,0,1,2]))
    print(solver.findMin(nums=[11,13,15,17]))
    print(solver.findMin(nums=[1]))
    print(solver.findMin(nums=[2,3,4,5,1]))
