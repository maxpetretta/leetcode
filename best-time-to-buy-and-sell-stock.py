from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force, O(n^2), O(1)
        # profit = 0
        # for i, buy in enumerate(prices):
        #     for j, sell in enumerate(prices[i:]):
        #         if sell - buy > profit:
        #             profit = sell - buy
        # return profit
        
        
        # Calculate profit while traversing list, O(n), O(1)
        profit = 0
        last_min = 0
        for i, price in enumerate(prices):
            if price < prices[last_min]:
                last_min = i
            elif profit < price - prices[last_min]:
                profit = price - prices[last_min]
        return profit


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxProfit(prices=[7,1,5,3,6,4]))
    print(solver.maxProfit(prices=[7,6,4,3,1]))
    print(solver.maxProfit(prices=[2,4,1]))
