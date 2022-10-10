from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Brute force, O(n), O(n)
        # answer = []
        
        # for i in range(1, n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         answer.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         answer.append("Fizz")
        #     elif i % 5 == 0:
        #         answer.append("Buzz")
        #     else:
        #         answer.append(str(i))
        # return answer
    
        # Use string concatenation, to handle extra conditions, O(n), O(n)
        # answer = []
        
        # for i in range(1, n+1):
        #     next = ""
            
        #     if i % 3 == 0:
        #         next += "Fizz"
        #     if i % 5 == 0:
        #         next += "Buzz"
            
        #     if next == "":
        #         answer.append(str(i))
        #     else:
        #         answer.append(next)
        # return answer

        # Use a hash map to hold the conditions, O(n), O(n)
        cond = {3: "Fizz", 5: "Buzz"}
        # divs = [3, 5] # Required prior to Python 3.7
        answer = []
        
        for i in range(1, n+1):
            next = ""
            for key in cond.keys():
                if i % key == 0:
                    next += cond[key]
            if next == "":
                answer.append(str(i))
            else:
                answer.append(next)
        return answer

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.fizzBuzz(3))
    print(solver.fizzBuzz(5))
    print(solver.fizzBuzz(15))
    print(solver.fizzBuzz(378))
