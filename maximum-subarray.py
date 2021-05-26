from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force, O(n^3)
        # length = len(nums)
        # total = sum(nums)
        # for size in reversed(range(1, length + 1)):
        #     for start in range(length - size + 1):
        #         window = sum(nums[start:start + size])
        #         if window > total:
        #             total = window
        # return total
        
        
        # Do not revisit past prefixes, O(n^2)
        # length = len(nums)
        # total = sum(nums)
        # for i in range(length):
        #     window = 0
        #     for j in range(i, length):
        #         window += nums[j]
        #         if window > total:
        #             total = window
        # return total
        

        # Divide and conquer, O(n log n)
        # def bestSubArray(nums: List[int], left: int, right: int) -> List[int]:
        #     if left > right:
        #         return -math.inf
            
        #     midpoint = math.floor((left + right) / 2)
            
        #     # Compute left half
        #     current = 0
        #     maxLeft = 0
        #     for i in reversed(range(left, midpoint)):
        #         current += nums[i]
        #         maxLeft = max(current, maxLeft)
            
        #     # Compute right half
        #     current = 0
        #     maxRight = 0
        #     for i in range(midpoint + 1, right + 1):
        #         current += nums[i]
        #         maxRight = max(current, maxRight)
            
        #     # Compute both sides
        #     maxBoth = nums[midpoint] + maxLeft + maxRight
            
        #     # Recurse and compute subarray sums
        #     subLeft = bestSubArray(nums, left, midpoint - 1)
        #     subRight = bestSubArray(nums, midpoint + 1, right)
        #     return max(maxBoth, subLeft, subRight)
        # return bestSubArray(nums, 0, len(nums) - 1)
        
        
        # Scan left to right, reseting when the current subarray is negative
        # Known as Kadane's algorithm, O(n)
        length = len(nums)
        current = nums[0]
        maximum = nums[0]
        for i in range(1, length):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            maximum = max(current, maximum)
        return maximum


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
    print(solver.maxSubArray(nums=[1]))
    print(solver.maxSubArray(nums=[5,4,-1,7,8]))
    print(solver.maxSubArray(nums=[-2,1]))
    print(solver.maxSubArray(nums=[5,-2,1,-3,4,-2,1]))
