from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force by sorting the array and iterating, O(n log n), O(1)
        # if not nums:
        #     return 0
        
        # nums.sort()
        # previous, streak, maximum = nums[0], 1, 1
        # for num in nums[1:]:
        #     if num == previous + 1:
        #         streak += 1
        #         maximum = max(maximum, streak)
        #     elif num == previous:
        #         continue
        #     else:
        #         streak = 1
        #     previous = num
        # return maximum


        # Transform array into a heap before counting, O(n), O(1)
        # if not nums:
        #     return 0
        
        # heapq.heapify(nums)
        # previous, streak, maximum = heapq.heappop(nums), 1, 1
        # while nums:
        #     num = heapq.heappop(nums)
        #     if num == previous + 1:
        #         streak += 1
        #         maximum = max(maximum, streak)
        #     elif num == previous:
        #         continue
        #     else:
        #         streak = 1
        #     previous = num
        # return maximum


        # Convert array into a set before counting, O(n), O(n)
        numSet = set(nums)
        maximum = 0
        
        for num in nums:
            if (num - 1) not in numSet:
                current, streak = num, 1
                
                while (current + 1) in numSet:
                    current += 1
                    streak += 1
                maximum = max(streak, maximum)
        return maximum


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.longestConsecutive(nums=[100,4,200,1,3,2]))
    print(solver.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
    print(solver.longestConsecutive(nums=[1,2,0,1]))
