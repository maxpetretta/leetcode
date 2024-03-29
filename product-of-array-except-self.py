from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force multiply each product, O(n^2), O(1)
        # length = len(nums)
        # answer = [1] * length
        # for i in range(length):
        #     for j in range(length):
        #         if i == j:
        #             continue
        #         else:
        #             answer[i] *= nums[j]
        # return answer
        
        
        # Compute products on the left and right sides of the index, O(n), O(n)
        # length = len(nums)
        # left, right, answer = [1] * length, [1] * length, [1] * length
        # for i in range(1, length):
        #     left[i] = left[i - 1] * nums[i - 1]
        # for i in reversed(range(length - 1)):
        #     right[i] = right[i + 1] * nums[i + 1]
        # for i in range(0, length):
        #     answer[i] = left[i] * right[i]
        # return answer
        
        
        # Use the left/right method, but with only 1 array, O(n), O(1)
        length = len(nums)
        answer = [1] * length
        right = 1
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]
        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]
        return answer


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.productExceptSelf(nums=[1,2,3,4]))
    print(solver.productExceptSelf(nums=[-1,1,0,-3,3]))
    print(solver.productExceptSelf(nums=[4,5,1,8,2]))
