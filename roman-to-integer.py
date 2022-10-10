class Solution:
    def romanToInt(self, s: str) -> int:
        # Brute force, O(1), O(1)
        # vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # answer = 0
        # i = 0
        
        # while i < len(s):
        #     if i+1 < len(s) and vals[s[i]] < vals[s[i+1]]:
        #         answer += vals[s[i+1]] - vals[s[i]]
        #         i += 2
        #     else:
        #         answer += vals[s[i]]
        #         i += 1
        # return answer
        
        # Do a left-to-right pass w/ expanded symbols, O(1), O(1)
        # vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": "900"}
        # answer = 0
        # i = 0
        
        # while i < len(s):
        #     if len(s) - i >= 2 and s[i:i+2] in vals:
        #         answer += int(vals[s[i:i+2]])
        #         i += 2
        #     else:
        #         answer += vals[s[i]]
        #         i += 1
        # return answer
    
        # Do a right-to-left pass, starting from the second-to-last index, O(1), O(1)
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = vals[s[-1]]
        
        for i in reversed(range(0, len(s)-1)):
            if vals[s[i]] < vals[s[i+1]]:
                answer -= vals[s[i]]
            else:
                answer += vals[s[i]]
        return answer
        
# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.romanToInt("III"))
    print(solver.romanToInt("LVIII"))
    print(solver.romanToInt("MCMXCIV"))
    print(solver.romanToInt("MMMDCCCLXXXVIII"))
