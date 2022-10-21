from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Send every person to city a, then calculate refund amounts to go to city b 
        instead.  Take the top n refunds and add to the total.  O(n), O(n)
        """
        # n = len(costs) // 2
        # total = sum([x for x, y in costs])
        # refunds = [y - x for x, y in costs]
        
        # refunds.sort()
        # for i in range(n):
        #     total += refunds[i]
        # return total


        # Use a greedy algorithm to choose which city, O(n), O(1)
        costs.sort(key = lambda x: x[0] - x[1])
        
        total, n = 0, len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.twoCitySchedCost(costs=[[10,20],[30,200],[400,50],[30,20]]))
    print(solver.twoCitySchedCost(costs=[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
    print(solver.twoCitySchedCost(costs=[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
    