from collections import Counter, defaultdict


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
        
        """
        Build an occurrence hashmap of t.  Using a sliding window over s,
        check if each character condition is met.  Return the smallest substring
        O(m + n), O(m + n)
        """
        window, chars = defaultdict(int), Counter(t)
        have, need = 0, len(chars)
        left, answer = 0, ""
        
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in chars and window[char] == chars[char]:
                have += 1
            
            while have == need:
                # Check for new smallest substring
                if (right - left + 1) < len(answer) or answer == "":
                    answer = s[left:right + 1]
                
                # Shift window left
                window[s[left]] -= 1
                if s[left] in chars and window[s[left]] < chars[s[left]]:
                    have -= 1
                left += 1
        return answer
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solver.minWindow(s="a", t="a"))
    print(solver.minWindow(s="a", t="aa"))
    print(solver.minWindow(s="bbaa", t="aba"))
