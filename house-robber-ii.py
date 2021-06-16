from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Brute force, O(2 ^ n)
        # def robHouse(nums, i):
        #     maximum = -1
        #     if i == len(nums):
        #         maximum = 0
        #     elif i == len(nums) - 1:
        #         maximum = nums[i]
        #     else:
        #         takeHouse = nums[i] + robHouse(nums, i + 2)
        #         skipHouse = robHouse(nums, i + 1)
        #         maximum = max(takeHouse, skipHouse)
        #     return maximum
        
        # if len(nums) == 1:
        #     return nums[0]
        
        # withLast = robHouse(nums[:-1], 0)
        # withoutLast = robHouse(nums[1:], 0)
        # return max(withLast, withoutLast)
        
        
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
        
        # if len(nums) == 1:
        #     return nums[0]
        
        # withLast = robHouse(nums[:-1], 0, {})
        # withoutLast = robHouse(nums[1:], 0, {})
        # return max(withLast, withoutLast)
        
        
        # Dynamic programming with two pointers, O(n), O(1)
        def robHouse(nums):
            pt1, pt2 = 0, 0
            for num in nums:
                current = max(pt1, num + pt2)
                pt2 = pt1
                pt1 = current
            return pt1
            
        if len(nums) == 1:
            return nums[0]
        
        withLast = robHouse(nums[:-1])
        withoutLast = robHouse(nums[1:])
        
        return max(withLast, withoutLast)
        
        
# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.rob(nums=[2,3,2]))
    print(solver.rob(nums=[1,2,3,1]))
    print(solver.rob(nums=[0]))
    print(solver.rob(nums=[1,2,1,1]))
    print(solver.rob(nums=[200,3,140,20,10]))
