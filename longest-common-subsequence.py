class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brute force would be generating all subsequences of text1,
        # and checking for their existence in text2, O(2 ^ len(text1))
        
        
        # Use recursion w/ memoization, O(len(text1) * len(text2)^2)
        # Side note: Instead of implementing a memoization table, can use ->
        # @lru_cache(maxsize=None)
#         def lcs(text1, text2, memo):
#             if len(text1) == 0 or len(text2) == 0:
#                 return 0
#             elif (text1 + ":" + text2) in memo:
#                 return memo[text1 + ":" + text2]

#             letter = text1[0:1]
#             excludesLetter = lcs(text1[1:], text2, memo)

#             includesLetter = 0
#             if letter in text2:
#                 includesLetter = lcs(text1[1:], text2[text2.index(letter) + 1:], memo) + 1

#             memo[text1 + ":" + text2] = max(includesLetter, excludesLetter)
#             return memo[text1 + ":" + text2]
        
#         memo = {}
#         return lcs(text1, text2, memo)
        
        
        # Refined memoization, accounting for same first character matches
        # O(len(text1) * len(text2))
#         def lcs(text1, text2, memo):
#             if len(text1) == 0 or len(text2) == 0:
#                 return 0
#             elif (text1 + ":" + text2) in memo:
#                 return memo[text1 + ":" + text2]
#             elif text1[0] == text2[0]:
#                 return lcs(text1[1:], text2[1:], memo) + 1
#             else:
#                 memo[text1 + ":" + text2] = max(lcs(text1[1:], text2, memo),
#                                                 lcs(text1, text2[1:], memo))
#                 return memo[text1 + ":" + text2]
        
#         memo = {}
#         return lcs(text1, text2, memo)


        # Bottom up dynamic programming, compute previous answer grid
        # O(len(text1) * len(text2)), O(len(text1) * len(text2))
#         length1, length2 = len(text1), len(text2)
#         grid = [[0] * (length2+1) for i in range(length1+1)]
#         for j in reversed(range(length2)):      # Columns
#             for i in reversed(range(length1)):  # Rows 
#                 if text1[i] == text2[j]:
#                     grid[i][j] = grid[i+1][j+1] + 1
#                 else:
#                     grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        
#         return grid[0][0]


        # Optimize space by only tracking the previous column
        # O(len(text1) * len(text2)), O(min(len(text1) * len(text2)))
            
        length1, length2 = len(text1), len(text2)
        previous = [0] * (length1 + 1)
        current = [0] * (length1 + 1)
        for j in reversed(range(length2)):      # Columns
            for i in reversed(range(length1)):  # Rows 
                if text1[i] == text2[j]:
                    current[i] = previous[i+1] + 1
                else:
                    current[i] = max(previous[i], current[i+1])
            previous, current = current, previous
        
        return previous[0]


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.longestCommonSubsequence(text1="abcde", text2="ace"))
    print(solver.longestCommonSubsequence(text1="abc", text2="abc"))
    print(solver.longestCommonSubsequence(text1="abc", text2="def"))
    print(solver.longestCommonSubsequence(text1="ezupkr", text2="ubmrapg"))
    print(solver.longestCommonSubsequence(text1="oxcpqrsvwf", text2="shmtulqrypy"))
