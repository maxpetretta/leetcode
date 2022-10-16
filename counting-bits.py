from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Brute force using the Hamming weight, O(n log n), O(1)
        # answer = []
        
        # for i in range(n + 1):
        #     ans.append(self.hammingWeight(i))
        # return answer
    
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n > 0:
    #         n &= (n - 1)
    #         count += 1
    #     return count


        # Remove most significant bit, O(n), O(1)
        # answer = [0] * (n + 1)
        
        # for i in range(1, n + 1):
        #     answer[i] = answer[i >> 1] + (i & 1)
        # return answer
        
        
        # Remove least significant bit, O(n), O(1)
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
