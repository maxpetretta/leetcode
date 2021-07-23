from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute force, O(nm^3 - mn^3), O(1)
        # def contains(s, t):
        #     for char in t:
        #         if t.count(char) <= s.count(char):
        #             continue
        #         else:
        #             return False
        #     return True
        
        # m, n = len(s), len(t)
        # ans = ""
        # for i in range(m):
        #     for j in range(i+n, m+1):
        #         sub = s[i:j]
        #         if contains(sub, t) and (len(sub) < len(ans) or ans == ""):
        #             ans = sub
        # return ans
        
        
        # Two pointers, O(m + n), O(m + n)
        def contains(s, t):
            for char in t.keys():
                if t[char] > s[char]:
                    return False
            return True
        
        m, n = len(s), len(t)
        l, r = 0, n-1
        chars, window = Counter(t), Counter(s[l:r+1])
        ans = ""
        
        while r < m:
            sub = s[l:r+1]

            if contains(window, chars):
                window[s[l]] = window.get(s[l], 0) - 1
                l += 1
                if len(sub) < len(ans) or ans == "":
                    ans = sub
            else:
                r += 1
                if r < m:
                    window[s[r]] = window.get(s[r], 0) + 1
        return ans
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solver.minWindow(s="a", t="a"))
    print(solver.minWindow(s="a", t="aa"))
    print(solver.minWindow(s="bbaa", t="aba"))
