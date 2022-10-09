from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force, compare every number pair, O(n^2), O(1)
        # for i, a in enumerate(nums):
        #     for j, b in enumerate(nums):
        #         if i != j and a + b == target:
        #             return [i, j]
        
        # Do not check previously visited combinations, O(n^2), O(1)
        # runs = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j + runs:
        #             continue
        #         elif j + runs >= len(nums):
        #             break
        #         elif nums[i] + nums[j + runs] == target:
        #             return [i, j + runs]
        #     runs += 1
        
        # Build a hashmap of complements, O(n), O(n)
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [i, complements[complement]]
            complements[num] = i
    

# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.twoSum(nums=[2,7,11,15], target=9))
    print(solver.twoSum(nums=[3,2,4], target=6))
    print(solver.twoSum(nums=[3,3], target=6))
    print(solver.twoSum(nums=[-1,-2,-3,-4,-5], target=-8))
