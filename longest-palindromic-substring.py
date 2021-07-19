class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force, O(n^3), O(1)
        # maximum = s[0]
        # length = len(s)
        
        # for i in range(length):
        #     for j in range(i+1, length+1):
        #         sub = s[i:j]
        #         if sub == sub[::-1] and len(sub) > len(maximum):
        #             maximum = sub
                    
        # return maximum
        
        
        # Expand around the center of the substring, O(n^2), O(1)
        def expand(s, l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        sub = s[0]
        
        for i in range(len(s)):
            subOdd = expand(s, i, i) # check odd strings
            subEven = expand(s, i, i+1) # check even strings
            subMax = max(subOdd, subEven, key=len)
            
            if len(subMax) > len(sub):
                sub = subMax
            
        return sub


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.longestPalindrome(s="babad"))
    print(solver.longestPalindrome(s="cbbd"))
    print(solver.longestPalindrome(s="a"))
    print(solver.longestPalindrome(s="ac"))
    print(solver.longestPalindrome(s="SQQSYYSQQS"))
