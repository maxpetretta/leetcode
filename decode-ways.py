class Solution:
    def numDecodings(self, s: str) -> int:
        # Brute force, O(2 ^ n), O(n)
        # def decode(s):
        #     if len(s) == 0:
        #         return 1
        #     elif s[0] == "0":
        #         return 0
        #     elif len(s) == 1:
        #         return 1
        #     else:
        #         ways = decode(s[1:])
        #         if int(s[0:2]) <= 26:
        #             ways += decode(s[2:])
        #         return ways
        
        # return decode(s)

    
        # Add memoization, O(n), O(n)
        # def decode(s, memo):
        #     if len(s) == 0:
        #         return 1
        #     elif s[0] == "0":
        #         return 0
        #     elif s in memo:
        #         return memo[s]
        #     elif len(s) == 1:
        #         memo[s] = 1
        #         return 1
        #     else:
        #         ways = decode(s[1:], memo)
        #         if int(s[0:2]) <= 26:
        #             ways += decode(s[2:], memo)
        #         memo[s] = ways
        #         return ways
        
        # return decode(s, {})


        # Iterative approach, O(n), O(n)
        # ways = [0] * (len(s) + 1)
        # ways[0] = 1
        
        # if s[0] == "0":
        #     return 0
        # elif int(s[0]) > 0:
        #     ways[1] = 1
        
        # for i in range(2, len(ways)):
        #     if int(s[i-1]) > 0:
        #         ways[i] += ways[i-1]
        #     if 10 <= int(s[i-2:i]) <= 26:
        #         ways[i] += ways[i-2]

        # return ways[-1]
    
    
        # Iterative in constant space, O(n), O(1)
        previous = 1
        current = 0 if s[0] == "0" else 1
        
        if s[0] == "0":
            return 0
        
        for i in range(2, len(s)+1):
            ways = 0
            if int(s[i-1]) > 0:
                ways += current
            if 10 <= int(s[i-2:i]) <= 26:
                ways += previous
            previous = current
            current = ways

        return current


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.numDecodings(s="12"))
    print(solver.numDecodings(s="226"))
    print(solver.numDecodings(s="0"))
    print(solver.numDecodings(s="06"))
    print(solver.numDecodings(s="2101"))
