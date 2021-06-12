import math
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Brute force, O(2 ^ n)
        # def countLIS(nums, index, previous):
        #     if index == len(nums):
        #         return 0
        #     countA = 0
        #     if nums[index] > previous:
        #         countA = countLIS(nums, index + 1, nums[index]) + 1
        #     countB = countLIS(nums, index + 1, previous)
        #     return max(countA, countB)
        
        # return countLIS(nums, 0, -math.inf)
    
        
        # Use memoization, O(n ^ 2)
        # def countLIS(nums, index, previous, memo):
        #     if index == len(nums):
        #         return 0
        #     elif memo[previous + 1][index] > 0:
        #         return memo[previous + 1][index]
            
        #     countA = 0
        #     if previous < 0 or nums[index] > nums[previous]:
        #         countA = countLIS(nums, index + 1, index, memo) + 1
        #     countB = countLIS(nums, index + 1, previous, memo)
        #     memo[previous + 1][index] = max(countA, countB)
        #     # print(memo[previous + 1][index])
        #     return memo[previous + 1][index]
        
        # memo = [[0] * len(nums) for i in range(len(nums))]
        # return countLIS(nums, 0, -1, memo)
        
        
        # Keep track of longest subsequence, O(n ^ 2)
        # length = len(nums)
        # if length == 0:
        #     return 0
        
        # seq = [0] * length
        # seq[0] = 1
        # maximum = 1
        # for i in range(1, length):
        #     value = 0
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             value = max(seq[j], value)
        #     seq[i] = value + 1
        #     maximum = max(seq[i], maximum)
        # return maximum

        
        # Keep track again, but use binary search, O(n log n)
        length = len(nums)
        if length == 0:
            return 0
        
        seq = [0] * length
        size = 0
        for num in nums:
            i, j = 0, size
            while i != j:
                mid = (i + j) // 2
                if seq[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            seq[i] = num
            size = max(i + 1, size)
        return size


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))
    print(solver.lengthOfLIS(nums=[0,1,0,3,2,3]))
    print(solver.lengthOfLIS(nums=[7,7,7,7,7,7,7]))
    print(solver.lengthOfLIS(nums=[0]))
