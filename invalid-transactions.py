from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        Track past transactions by a user with a hashmap, and invalid transactions
        using a set.  For every transaction, check against criteria and past
        user transactions, O(n^2), O(n)
        """
        users, invalid = defaultdict(list), set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            
            # Check current transaction amount
            if int(amount) > 1000:
                invalid.add(i)
            
            # Check past transactions by user
            for j in users[name]:
                pName, pTime, pAmount, pCity = transactions[j].split(",")
                if abs(int(time) - int(pTime)) <= 60 and city != pCity:
                    invalid.add(i)
                    invalid.add(j)
            users[name].append(i)
        
        # Build the result list
        return [transactions[i] for i in invalid]
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.invalidTransactions(transactions=["alice,20,800,mtv","alice,50,100,beijing"]))
    print(solver.invalidTransactions(transactions=["alice,20,800,mtv","alice,50,1200,mtv"]))
    print(solver.invalidTransactions(transactions=["alice,20,800,mtv","bob,50,1200,mtv"]))
    print(solver.invalidTransactions(transactions=["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]))
    print(solver.invalidTransactions(transactions=["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
