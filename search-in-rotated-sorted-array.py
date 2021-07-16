from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force, O(n), O(1)
        # index = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         index = i
        # return index
    
    
        # Binary search, O(log n), O(1)
        def binSearch(nums, target, start, end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif start > end:
                return -1
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    return binSearch(nums, target, start, mid - 1)
                else:
                    return binSearch(nums, target, mid + 1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return binSearch(nums, target, mid + 1, end)
                else: 
                    return binSearch(nums, target, start, mid - 1)
        
        return binSearch(nums, target, 0, len(nums) - 1)


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.search(nums=[4,5,6,7,0,1,2], target=0))
    print(solver.search(nums=[4,5,6,7,0,1,2], target=3))
    print(solver.search(nums=[1], target=0))
    print(solver.search(nums=[1,3], target=3))
