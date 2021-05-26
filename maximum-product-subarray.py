import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force, O(n^3)
        # length = len(nums)
        # total = -math.inf
        # for size in range(1, length + 1):
        #     for start in range(length - size + 1):
        #         product = math.prod(nums[start:start + size])
        #         total = max(product, total)
        # return total
                
        
        # Calculate products in one pass, O(n^2)
        # length = len(nums)
        # total = math.prod(nums)
        # if total > 0:
        #     return total
        # for start in range(length):
        #     product = 1
        #     for i in range(length - start):
        #         product *= nums[start + i]
        #         total = max(product, total)
        # return total
        
        
        # Keep track of product chains (positive and negative), O(n)
        length = len(nums)
        total = math.prod(nums)
        if total > 0:
            return total
        
        minimum = maximum = total = nums[0]
        for i in range(1, length):
            current = nums[i]
            newMin = min(current, minimum * current, maximum * current)
            maximum = max(current, minimum * current, maximum * current)
            minimum = newMin
            total = max(maximum, total)
        return total


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxProduct(nums=[2,3,-2,4]))
    print(solver.maxProduct(nums=[-2,0,-1]))
    print(solver.maxProduct(nums=[0]))
    print(solver.maxProduct(nums=[2,-5,3,1,-4,0,-10,2,8]))
