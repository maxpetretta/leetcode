from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force, O(n^2), O(1)
        # s = list(s)
        
        # if len(s) != len(t):
        #     return False
        
        # for char in t:
        #     if char in s:
        #         s.remove(char)
        
        # if len(s) == 0:
        #     return True


        # Sort the strings, O(n log n), O(1)
        # if len(s) != len(t):
        #     return False
        
        # s, t = sorted(s), sorted(t)
        
        # if s == t:
        #     return True
        # else:
        #     return False
        
        
        # Use a hashmap, O(n), O(1) since we are capped to 26 letters
        map = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for char in s:
            map[char] += 1        
        for char in t:
            map[char] -= 1
        
        if max(map.values()) > 0:
            return False
        else:
            return True


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.isAnagram(s="anagram", t="nagaram"))
    print(solver.isAnagram(s="rat", t="car"))
    print(solver.isAnagram(s="a", t="ab"))
