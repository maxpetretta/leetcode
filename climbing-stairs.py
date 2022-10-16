import math


class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute force using recursion, O(2^n), O(n)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        
        # Use recursion with memoization, O(n), O(n)
        # def climbStairsMemo(n, memo):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     elif n in memo:
        #         return memo[n]
        #     memo[n] = climbStairsMemo(n - 1, memo) + climbStairsMemo(n - 2, memo)
        #     return memo[n]
        
        # return climbStairsMemo(n, {})
    
        
        # Dynamically build memo map from previous results, O(n), O(n)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        
        # memo = {}
        # memo[1], memo[2] = 1, 2
        # for i in range(3, n + 1):
        #     memo[i] = memo[i - 1] + memo[i - 2]
        
        # return memo[n]
        
        
        # Recognize it's the Fibonacci sequence, O(n), O(1)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        
        # x, y = 1, 2
        # for i in range(3, n + 1):
        #     z = x + y
        #     x, y = y, z
        # return y
        
        
        # Use the Fibonacci formula, O(log n), O(1)
        sqrt5 = math.sqrt(5)
        val = math.pow((1+sqrt5) / 2, n+1) - math.pow((1-sqrt5) / 2, n+1)
        return int(val // sqrt5)


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.climbStairs(n=2))
    print(solver.climbStairs(n=3))
    print(solver.climbStairs(n=38))
