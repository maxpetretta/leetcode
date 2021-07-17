class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window, O(n), O(1)
        # freq = {}
        # left, maximum = 0, 0
        
        # for right in range(len(s)):
        #     freq[s[right]] = freq.get(s[right], 0) + 1
            
        #     while (right - left + 1) - max(freq.values()) > k:
        #         freq[s[left]] -= 1
        #         left += 1
        #     maximum = max((right - left + 1), maximum)
        # return maximum

    
        # Optimize by only moving window when maximum can be exceeded, O(n), O(1)
        freq = {}
        left, maximum, maxFreq = 0, 0, 0
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(freq[s[right]], maxFreq)
            
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            maximum = max((right - left + 1), maximum)
        return maximum


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.characterReplacement(s="ABAB", k=2))
    print(solver.characterReplacement(s="AABABBA", k=1))
