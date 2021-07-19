class Solution:
    def isValid(self, s: str) -> bool:
        # Keep a stack of open brackets, O(n), O(n)
        stack = []
        pairs = { ")": "(", "}": "{", "]": "[" }
        
        for b in s:
            if len(stack) > 0 and b in pairs:
                if stack[-1] == pairs[b]:
                    stack.pop()
                else:
                    return False
            elif b in pairs.values():
                stack.append(b)
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
