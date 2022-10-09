class Solution:
    def isValid(self, s: str) -> bool:
        # Keep a stack of open brackets, O(n), O(n)
        stack = []
        pairs = { ")": "(", "]": "[", "}": "{" }
        
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif stack and pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.isValid(s="()"))
    print(solver.isValid(s="()[]{}"))
    print(solver.isValid(s="(]"))
    print(solver.isValid(s="([)]"))
    print(solver.isValid(s="{[]}"))
    print(solver.isValid(s="))"))
