from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force compare every two heights, O(n^2), O(1)
        # maximum, length = 0, len(height)
        # for i in range(length - 1):
        #     for j in range(i+1, length):
        #         area = min(height[i], height[j]) * (j - i)
        #         maximum = max(area, maximum)
        # return maximum
    
    
        # Use left/right pointers moving inwards, O(n), O(1)
        maximum, length = 0, len(height)
        left, right = 0, length - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maximum = max(area, maximum)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
        

# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxArea(height=[1,8,6,2,5,4,8,3,7]))
    print(solver.maxArea(height=[1,1]))
    print(solver.maxArea(height=[4,3,2,1,4]))
    print(solver.maxArea(height=[1,2,1]))
    print(solver.maxArea(height=[1,2,4,3]))
