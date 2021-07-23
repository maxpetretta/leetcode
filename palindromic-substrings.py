class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute force, O(n^3), O(1)
        # count = 0
        # length = len(s)
        
        # for i in range(length):
        #     for j in range(i+1, length+1):
        #         sub = s[i:j]
        #         if sub == sub[::-1]:
        #             count += 1
        # return count

        
        # Dynamic programming, O(n^2), O(n^2)
        # count = 0
        # length = len(s)
        # dp = [[False for i in range(length)] for j in range(length)]
        
        # for i in range(length):
        #     dp[i][i] = True
        #     count += 1
        
        # for i in range(length-1):
        #     if s[i] == s[i+1]:
        #         dp[i][i+1] = True
        #         count += 1
        
        # for k in range(3, length+1):
        #     for i in range(length-k+1):
        #         j = i + k - 1
        #         if dp[i+1][j-1] and s[i] == s[j]:
        #             dp[i][j] = True
        #             count += 1
                
        # return count
                
        
        # Build substrings from the middle out, O(n^2), O(1)
        def expand(s, l, r):
            count = 0
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        
        count = 0
        length = len(s)
        
        for i in range(length):
            count += expand(s, i, i)
            count += expand(s, i, i+1)
        return count


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.countSubstrings(s="abc"))
    print(solver.countSubstrings(s="aaa"))
    print(solver.countSubstrings(s="aaaaa"))
