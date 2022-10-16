from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array and use two pointer method, O(n^2), O(1)
        # nums.sort()
        # length = len(nums)
        # answer = []
        
        # for i in range(length - 2):
        #     if nums[i] > 0:
        #         break
        #     elif i > 0 and nums[i] == nums[i - 1]:
        #         continue    
        #     left, right = i + 1, length - 1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
        #         if total < 0:
        #             left += 1
        #         elif total > 0:
        #             right -= 1
        #         else:
        #             answer.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        # return answer
        
        
        # Store a hashmap of complements, O(n^2), O(n)
        # nums.sort()
        # length = len(nums)
        # answer = []
        
        # for i in range(length - 2):
        #     if nums[i] > 0:
        #         break
        #     elif i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     complements = {}
        #     j = i + 1
        #     while j < length:
        #         complement = -nums[i] - nums[j]
        #         if complement in complements:
        #             answer.append([nums[i], nums[j], complement])
        #             while j + 1 < length and nums[j] == nums[j + 1]:
        #                 j += 1
        #         complements[nums[j]] = complement
        #         j += 1
        # return answer
        

        # Use hashsets to avoid sorting the array first, O(n^2), O(n)
        answer, duplicates = set(), set()
        seen = {}
        
        for i, numA in enumerate(nums):
            if numA not in duplicates:
                duplicates.add(numA)
                for j, numB in enumerate(nums[i + 1:]):
                    complement = -numA - numB
                    if complement in seen and seen[complement] == i:
                        answer.add(tuple(sorted((numA, numB, complement))))
                    seen[numB] = i
        return answer


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.threeSum(nums=[-1,0,1,2,-1,-4]))
    print(solver.threeSum(nums=[]))
    print(solver.threeSum(nums=[0]))
    print(solver.threeSum(nums=[0,0,0]))
