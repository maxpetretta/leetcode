from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers method, O(n^2), O(n)
        # def twoSum(nums, i, triplets):
        #     low = i + 1
        #     high = len(nums) - 1
        #     while low < high:
        #         total = nums[i] + nums[low] + nums[high] 
        #         if total < 0:
        #             low += 1
        #         elif total > 0:
        #             high -= 1
        #         else:
        #             triplets.append([nums[i], nums[low], nums[high]])
        #             low += 1
        #             high -= 1
        #             while nums[low] == nums[low - 1] and low < high:
        #                 low += 1

        # triplets = []
        # length = len(nums)
        # nums.sort()
    
        # for i in range(length):
        #     if nums[i] > 0:
        #         break
        #     elif i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     else:
        #         twoSum(nums, i, triplets)
        # return triplets
        
        
        # Use a hashtable to store compliments, O(n^2), O(n)
        # def twoSum(nums, i, triplets):
        #     values = set()
        #     j = i + 1
        #     while j < len(nums):
        #         complement = -nums[i] - nums[j]
        #         if complement in values:
        #             triplets.append([nums[i], nums[j], complement])
        #             while j + 1 < len(nums) and nums[j] == nums[j + 1]:
        #                 j += 1
        #         values.add(nums[j])
        #         j += 1
        
        # triplets = []
        # length = len(nums)
        # nums.sort()
        
        # for i in range(length):
        #     if nums[i] > 0:
        #         break
        #     elif i == 0 or nums[i] != nums[i - 1]:
        #         twoSum(nums, i, triplets)
        # return triplets
        

        # Use a hashmap without sorting the array first, O(n^2), O(n)
        triplets, duplicates = set(), set()
        values = {}
        
        for i, numA in enumerate(nums):
            if numA not in duplicates:
                duplicates.add(numA)
                for j, numB in enumerate(nums[i+1:]):
                    complement = -numA - numB
                    if complement in values and values[complement] == i:
                        triplets.add(tuple(sorted((numA, numB, complement))))
                    values[numB] = i
        return triplets


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.threeSum(nums=[-1,0,1,2,-1,-4]))
    print(solver.threeSum(nums=[]))
    print(solver.threeSum(nums=[0]))
    print(solver.threeSum(nums=[0,0,0]))
