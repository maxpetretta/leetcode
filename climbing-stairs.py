import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute force, O(2 ^ n)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        
        # Recursive memoization, O(n)
        # def climbStairs(n, memo):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     elif memo[n] != 0:
        #         return memo[n]
        #     else:
        #         count = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
        #         memo[n] = count
        #         return count
        
        # return climbStairs(n, [0] * (n + 1))
    
        
        # Iterative memoization, O(n)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     memo = [0] * (n + 1)
        #     memo[1] = 1
        #     memo[2] = 2
        #     for i in range(3, n + 1):
        #         memo[i] = memo[i - 1] + memo[i - 2]
        #     return memo[n]
        
        
        # Recognize it's the Fibonacci sequence, O(n), O(1)
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     x = 1
        #     y = 2
        #     for i in range(3, n + 1):
        #         z = x + y
        #         x = y
        #         y = z
        #     return y
        
        
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
