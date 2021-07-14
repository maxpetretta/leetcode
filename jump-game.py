from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Brute force, O(2 ^ n), O(n)
        # def jump(nums, start):
        #     if start >= len(nums) - 1:
        #         return True
            
        #     reach = min(nums[start], len(nums) - 1)
        #     for i in reversed(range(1, reach + 1)):
        #         if jump(nums, start+i):
        #             return True
        #     return False
        
        # return jump(nums, 0)


        # Add memoization, O(n ^ 2), O(n)
        # def jump(nums, start, memo):
        #     if start in memo:
        #         return memo[start]
        #     elif start >= len(nums) - 1:
        #         return True
            
        #     reach = min(nums[start], len(nums) - 1)
        #     for i in reversed(range(1, reach + 1)):
        #         if jump(nums, start+i, memo):
        #             memo[start] = True
        #             return True
        #     memo[start] = False
        #     return False
        
        # return jump(nums, 0, {})

        
        # Bottom-up approach, O(n ^ 2), O(n)
        # length = len(nums)
        # memo = [False] * length
        # memo[length - 1] = True
        
        # for i in reversed(range(0, length - 1)):
        #     reach = min(nums[i] + i, length - 1)
        #     for j in range(i + 1, reach + 1):
        #         if memo[j]:
        #             memo[i] = True
        #             break
        
        # return memo[0]
    
    
        # Greedy algorithm, O(n), O(1)
        last = len(nums) - 1
        for i in reversed(range(0, last)):
            if nums[i] + i >= last:
                last = i
        
        return last == 0
    

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.canJump(nums=[2,3,1,1,4]))
    print(solver.canJump(nums=[3,2,1,0,4]))
    print(solver.canJump(nums=[1,2,3]))
    print(solver.canJump(nums=[9,4,2,1,0,2,0]))
