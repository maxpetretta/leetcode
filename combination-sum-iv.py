from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Brute force, O(target * n ^ 2)
        # def findCombination(nums, remainder):
        #     ways = 0
        #     for num in nums:
        #         if remainder - num < 0:
        #             break
        #         elif remainder - num == 0:
        #             ways += 1
        #         else:
        #             ways += findCombination(nums, remainder - num)
        #     return ways
        
        # nums.sort()
        # return findCombination(target * n)

    
        # Add memoization, O(target * n)
        # def findCombination(nums, remainder, memo):
        #     ways = 0
        #     for num in nums:
        #         if remainder - num < 0:
        #             break
        #         elif remainder - num == 0:
        #             ways += 1
        #         elif remainder in memo:
        #             return memo[remainder]
        #         else:
        #             ways += findCombination(nums, remainder - num, memo)
        #     memo[remainder] = ways
        #     return memo[remainder]
        
        # nums.sort()
        # memo = {}
        # return findCombination(nums, target, memo)
    
        
        # Dynamic programming, O(target * n)
        nums.sort()
        ways = [0 for i in range(target + 1)]
        ways[0] = 1
        
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    ways[i] += ways[i - num]
                else:
                    break
        return ways[target]
    

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.combinationSum4(nums=[1,2,3], target=4))
    print(solver.combinationSum4(nums=[9], target=3))
    print(solver.combinationSum4(nums=[4,2,1], target=32))
