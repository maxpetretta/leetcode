from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Brute force with hamming weight, O(nb)
        # answer = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     count = 0
        #     current = i
        #     while current > 0:
        #         current &= (current - 1)
        #         count += 1
        #     answer[i] = count
        # return answer
        
        
        # Remove most significant bit, O(n)
        # answer = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     answer[i] = answer[i >> 1] + (i & 1)
        # return answer
        
        
        # Remove least significant bit, O(n)
        answer = [0] * (n + 1)
        for i in range(1, n + 1):
            answer[i] = answer[i & (i - 1)] + 1
        return answer


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.countBits(n=2))
    print(solver.countBits(n=5))
    print(solver.countBits(n=33))
    print(solver.countBits(n=256))
