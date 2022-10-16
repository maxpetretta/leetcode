class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force check every possible substring, O(n^3), O(n)
        # def uniqueSubstring(s) -> bool:
        #     chars = set()
        #     for char in s:
        #         if char in chars:
        #             return False
        #         else:
        #             chars.add(char)
        #     return True
        
        # length, maximum = len(s), 0
        # for i in range(length):
        #     for j in range(i, length):
        #         if uniqueSubstring(s[i:j+1]):
        #             maximum = max(j - i + 1, maximum)
        # return maximum
        
        
        # Use a set to track the substring in the sliding window, O(n), O(n)
        chars, maximum = set(), 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maximum = max(right - left + 1, maximum)
            right += 1
        return maximum


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring(s="abcabcbb"))
    print(solver.lengthOfLongestSubstring(s="bbbbb"))
    print(solver.lengthOfLongestSubstring(s="pwwkew"))
    print(solver.lengthOfLongestSubstring(s=""))
    print(solver.lengthOfLongestSubstring(s="aabaab!bb"))
