from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force, O(2 ^ n)
        # def searchWord(s, words, start):
        #     if start == len(s):
        #         return True
        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in words and searchWord(s, words, end):
        #             return True
        #     return False
                
        # return searchWord(s, set(wordDict), 0)
        
        
        # Add memoization, O(n ^ 3)
        # def searchWord(s, words, start, memo):
        #     if start == len(s):
        #         return True
        #     elif start in memo:
        #         return memo[start]
        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in words and searchWord(s, words, end, memo):
        #             memo[start] = True
        #             return memo[start]
        #     memo[start] = False
        #     return memo[start]
                
        # return searchWord(s, set(wordDict), 0, {})
    
    
        # Use breadth first search, O(n ^ 3)
        # queue = []
        # visited = set()
        # words = set(wordDict)
        
        # queue.append(0)
        # while queue:
        #     start = queue.pop(0)
        #     if start in visited:
        #         continue
        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in words:
        #             queue.append(end)
        #             if end == len(s):
        #                 return True
        #         visited.add(start)
        # return False

    
        # Dynamic programming, O(n ^ 3)
        words = set(wordDict)
        answer = [False] * (len(s) + 1)
        answer[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if answer[j] and s[j:i] in words:
                    answer[i] = True
                    break
        
        return answer[len(s)]


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.wordBreak(s="leetcode", wordDict=["leet","code"]))
    print(solver.wordBreak(s="applepenapple", wordDict=["apple","pen"]))
    print(solver.wordBreak(s="catsandog", wordDict=["cats","dog","sand","and","cat"]))
    print(solver.wordBreak(s="cars", wordDict=["car","ca","rs"]))
