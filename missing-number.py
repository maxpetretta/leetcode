from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute force, O(n log n)
        # nums.sort()
        # length = len(nums)
        # for i in range(length):
        #     if nums[i] != i:
        #         return i
        # return length
    
        
        # Use set containment, O(n)
        # numSet = set(nums)
        # length = len(nums) + 1
        # for num in range(length):
        #     if num not in numSet:
        #         return num
        
        
        # Use XOR, O(n)
        # value = len(nums)
        # for i, num in enumerate(nums):
        #     value ^= i ^ num
        # return value
        
        
        # Gauss' formula, O(n)
        expected = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)
        return expected - actual


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.missingNumber(nums=[3,0,1]))
    print(solver.missingNumber(nums=[0,1]))
    print(solver.missingNumber(nums=[9,6,4,2,3,5,7,0,1]))
    print(solver.missingNumber(nums=[0]))
