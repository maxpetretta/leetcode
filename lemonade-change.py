from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Greedy algorithm, try largest bills before smaller ones, O(n), O(1)
        change = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            if bill == 5:
                change[bill] += 1
            elif bill == 10 and change[5] > 0:
                change[5] -= 1
                change[bill] += 1
            else:
                if change[5] and change[10]:
                    change[10] -= 1
                    change[5] -= 1
                    change[bill] += 1
                elif change[5] >= 3:
                    change[5] -= 3
                    change[bill] += 1
                else:
                    return False
        return True

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.lemonadeChange([5,5,5,10,20]))
    print(solver.lemonadeChange([5,5,10,10,20]))
    print(solver.lemonadeChange([10, 10]))
    print(solver.lemonadeChange([5,5,5,5,20,20,5,5,20,5]))
