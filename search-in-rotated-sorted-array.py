from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force search, O(n), O(1)
        # index = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         index = i
        # return index
    
    
        # Optimize binary search to account for the pivot, O(log n), O(1)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Left side
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Right side
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.search(nums=[4,5,6,7,0,1,2], target=0))
    print(solver.search(nums=[4,5,6,7,0,1,2], target=3))
    print(solver.search(nums=[1], target=0))
    print(solver.search(nums=[1,3], target=3))
