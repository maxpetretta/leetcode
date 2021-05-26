from typing import List

class Solution:
    # Brute force, O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, numA in enumerate(nums):
    #         for j, numB in enumerate(nums):
    #             if i == j:
    #                 continue
    #             elif numA + numB == target:
    #                 return [i, j]


    # Do not check sum of previously visited combinations, O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     runs = 0
    #     for i, numA in enumerate(nums):
    #         for j, numB in enumerate(nums):
    #             if i == j + runs:
    #                 continue
    #             elif j + runs >= len(nums):
    #                 break
    #             elif nums[i] + nums[j + runs] == target:
    #                 return [i, j + runs]
    #         runs += 1
        
        
    # Build a hashmap of compliments, O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[num] = i
    

# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.twoSum(nums=[2,7,11,15], target=9))
    print(solver.twoSum(nums=[3,2,4], target=6))
    print(solver.twoSum(nums=[3,3], target=6))
    print(solver.twoSum(nums=[-1,-2,-3,-4,-5], target=-8))
