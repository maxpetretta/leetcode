from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute force with sorting, O(n log n), O(1)
        # nums.sort()
        # length = len(nums)
        # for i in range(length):
        #     if nums[i] != i:
        #         return i
        # return length
    
        
        # Compare each num with a set of distinct values, O(n), O(n)
        # distinct = set(nums)
        # for i in range(len(nums) + 1):
        #     if i not in distinct:
        #         return i
        
        
        # Use XOR to find the inverse, O(n), O(1)
        # value = len(nums)
        # for i, num in enumerate(nums):
        #     value ^= i ^ num
        # return value
        
        
        # Recognize it's Gauss' formula, O(n), O(1)
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
