from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a sliding window where k extra characters are allowed, O(n), O(1)
        # frequency = defaultdict(int)
        # left, maximum = 0, 0
        
        # for right in range(len(s)):
        #     frequency[s[right]] += 1
            
        #     while (right - left + 1) - max(frequency.values()) > k:
        #         frequency[s[left]] -= 1
        #         left += 1
        #     maximum = max((right - left + 1), maximum)
        # return maximum

    
        # Optimize by only moving the window when a higher frequency is reached, O(n), O(1)
        frequency = defaultdict(int)
        left, maximum, maxFrequency = 0, 0, 0
        
        for right in range(len(s)):
            frequency[s[right]] += 1
            maxFrequency = max(frequency[s[right]], maxFrequency)
            
            while (right - left + 1) - maxFrequency > k:
                frequency[s[left]] -= 1
                left += 1
            maximum = max((right - left + 1), maximum)
        return maximum


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.characterReplacement(s="ABAB", k=2))
    print(solver.characterReplacement(s="AABABBA", k=1))
