from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force, O(n^2), O(1)
        # maxWater = 0
        # for i, h1 in enumerate(height):
        #     for j, h2 in enumerate(height[i+1:], start=i+1):
        #         length = j - i
        #         area = min(h1, h2) * length
        #         maxWater = max(area, maxWater)
        # return maxWater
    
    
        # Two pointer method, O(n), O(1)
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            maxWater = max(min(height[start], height[end]) * (end - start), maxWater)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxWater
        

# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxArea(height=[1,8,6,2,5,4,8,3,7]))
    print(solver.maxArea(height=[1,1]))
    print(solver.maxArea(height=[4,3,2,1,4]))
    print(solver.maxArea(height=[1,2,1]))
    print(solver.maxArea(height=[1,2,4,3]))
