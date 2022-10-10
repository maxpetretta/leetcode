class Solution:
    def intToRoman(self, num: int) -> str:
        # Brute force, O(1), O(1)
        # vals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        # remainder = num
        # answer = ""
        
        # while remainder > 0:
        #     for key in reversed(vals.keys()):
        #         if key <= remainder:
        #             remainder -= key
        #             answer += vals[key]
        # return answer
        
        # Use a hardcoded table of digit values, O(1), O(1)
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]
        
        answer = thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]
        return answer

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.intToRoman(3))
    print(solver.intToRoman(58))
    print(solver.intToRoman(1994))
    print(solver.intToRoman(3999))
