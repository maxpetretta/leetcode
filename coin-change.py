import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Brute force recursive backtracking, O(amount ^ len(coins))
        # def change(coins, amount):
        #     if amount < 0:
        #         return -1
        #     elif amount == 0:
        #         return 0
            
        #     minimum = math.inf
        #     for coin in coins:
        #         count = change(coins, amount - coin)
        #         if count != -1:
        #             minimum = min(count + 1, minimum)
        #     if minimum == math.inf:
        #         return -1
        #     else:
        #         return minimum
        
        # return change(coins, amount)
    
    
        # Memoization, from the top down, O(amount * len(coins))
        # def change(coins, amount, memo):
        #     if amount < 0:
        #         return -1
        #     elif amount == 0:
        #         return 0
        #     elif memo[amount] != 0:
        #         return memo[amount]
            
        #     minimum = math.inf
        #     for coin in coins:
        #         count = change(coins, amount - coin, memo)
        #         if count != -1:
        #             minimum = min(count + 1, minimum)
            
        #     memo[amount] = minimum
        #     if minimum == math.inf:
        #         return -1
        #     else:
        #         return minimum
        
        # return change(coins, amount, [0] * (amount + 1))
        
        
        # Memoization, from the bottom up, O(amount * len(coins))
        memo = [math.inf] * (amount + 1)
        memo[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        if memo[amount] == math.inf:
            return -1
        else:
            return memo[amount]
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.coinChange(coins=[1,2,5], amount=11))
    print(solver.coinChange(coins=[2], amount=3))
    print(solver.coinChange(coins=[1], amount=0))
    print(solver.coinChange(coins=[1], amount=1))
    print(solver.coinChange(coins=[1], amount=2))
    print(solver.coinChange(coins=[1,2,5], amount=100))
