class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute force, O(n ^ 3), O(n)
        # def validSubstring(s):
        #     chars = set()
        #     for char in s:
        #         if char in chars:
        #             return False
        #         else:
        #             chars.add(char)
        #     return True
        
        # length = len(s)
        # maximum = 0
        
        # for i in range(length):
        #     for j in range(i, length):
        #         if validSubstring(s[i:j+1]):
        #             maximum = max(j - i + 1, maximum)
        # return maximum
        
        
        # Store used characters, O(n), O(n)
        maximum = 0
        chars = []
        
        for char in s:
            if char in chars:
                index = chars.index(char)
                chars = chars[index+1:]
                chars.append(char)
            else:
                chars.append(char)
            if len(chars) > maximum:
                maximum = len(chars)
        return maximum


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring(s="abcabcbb"))
    print(solver.lengthOfLongestSubstring(s="bbbbb"))
    print(solver.lengthOfLongestSubstring(s="pwwkew"))
    print(solver.lengthOfLongestSubstring(s=""))
    print(solver.lengthOfLongestSubstring(s="aabaab!bb"))
