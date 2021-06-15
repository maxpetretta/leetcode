from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Brute force, O(2 ^ n)
        # def robHouse(nums):
        #     maximum = -1
        #     if len(nums) == 0:
        #         maximum = 0
        #     elif len(nums) == 1:
        #         maximum = nums[0]
        #     else:
        #         takeHouse = nums[0] + robHouse(nums[2:])
        #         skipHouse = robHouse(nums[1:])
        #         maximum = max(takeHouse, skipHouse)
        #     return maximum
        
        # return robHouse(nums)
    
        
        # Add memoization, O(n)
        # def robHouse(nums, i, memo):
        #     maximum = -1
        #     if i == len(nums):
        #         maximum = 0
        #     elif i == len(nums) - 1:
        #         maximum = nums[i]
        #     elif i in memo:
        #         return memo[i]
        #     else:
        #         takeHouse = nums[i] + robHouse(nums, i + 2, memo)
        #         skipHouse = robHouse(nums, i + 1, memo)
        #         maximum = max(takeHouse, skipHouse)
            
        #     memo[i] = maximum
        #     return memo[i]
        
        # return robHouse(nums, 0, {})
        
        
        # Dynamic programming, O(n)
        # length = len(nums)
        # if length == 0:
        #     return 0
        
        # robbed = [-1] * (length + 1)
        # robbed[length] = 0
        # robbed[length - 1] = nums[length - 1]
        
        # for i in range(length - 2, -1, -1):
        #     robbed[i] = max(robbed[i + 1], robbed[i + 2] + nums[i])
        # return robbed[0]
    
    
        # Optimize for space, O(n), O(1)
        length = len(nums)
        if length == 0:
            return 0
        
        robbedPrev = 0
        robbed = nums[length - 1]
        
        for i in range(length - 2, -1, -1):
            current = max(robbed, robbedPrev + nums[i])
            robbedPrev = robbed
            robbed = current
            
        return robbed
    

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.rob(nums=[1,2,3,1]))
    print(solver.rob(nums=[2,7,9,3,1]))
    print(solver.rob(nums=[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
