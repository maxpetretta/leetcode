from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute force, O(n^2), O(1)
        # for i, numA in enumerate(nums):
        #     for j, numB in enumerate(nums):
        #         if i == j:
        #             continue
        #         elif numA == numB:
        #             return True
        # return False
        
        
        # Sort the list first, then iterate over it, O(n log n), O(1)
        # nums.sort()
        # last = None
        # for num in nums:
        #     if last == num:
        #         return True
        #     else:
        #         last = num
        # return False
        
        
        # Keep track of occurrences while iterating over list, O(n), O(n)
        occurrences = {}
        for i, num in enumerate(nums):
            if num in occurrences:
                return True
            else:
                occurrences[num] = True
        return False


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.containsDuplicate(nums=[1,2,3,1]))
    print(solver.containsDuplicate(nums=[1,2,3,4]))
    print(solver.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))
