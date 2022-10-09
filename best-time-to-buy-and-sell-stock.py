from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force, O(n^2), O(1)
        # profit = 0
        # for i, buy in enumerate(prices):
        #     for sell in prices[i:]:
        #         if sell - buy > profit:
        #             profit = sell - buy
        # return profit
        
        
        # Keep track of profit while traversing list, O(n), O(1)
        profit = 0
        minimum = prices[0]
        
        for price in prices:
            if price < minimum:
                minimum = price
            elif price - minimum > profit:
                profit = price - minimum
        return profit


# Testcases
if __name__ == '__main__':
    solver = Solution()
    print(solver.maxProfit(prices=[7,1,5,3,6,4]))
    print(solver.maxProfit(prices=[7,6,4,3,1]))
    print(solver.maxProfit(prices=[2,4,1]))
