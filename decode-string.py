class Solution:
    def decodeString(self, s: str) -> str:
        """
        Track each k segment using a stack, decoding when ] is reached
        O(max(k)^len(k) * n), O(sum(max(k)^len(k) * n))
        """
        # stack = []
        # for c in s:
        #     if c != "]":
        #         stack.append(c)
        #     else:
        #         segment = ""
        #         while stack and stack[-1] != "[":
        #             segment = stack.pop() + segment
        #         stack.pop()
                
        #         k = ""
        #         while stack and stack[-1].isdigit():
        #             k = stack.pop() + k
        #         k = int(k)
                
        #         stack.append(segment * k)
        # return "".join(stack)
        
        
        """
        Store both the current segment and k on the stack, decoding when ] is reached
        O(max(k) * n), O(m + n) where m = number of letters and n = number of digits
        """
        stack = []
        current, k = "", 0
        for c in s:
            if c == "[":
                stack.append((current, k))
                current, k = "", 0
            elif c == "]":
                segment, count = stack.pop()
                current = segment + (count * current)
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                current += c
        return current
        

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.decodeString(s="3[a]2[bc]"))
    print(solver.decodeString(s="3[a2[c]]"))
    print(solver.decodeString(s="2[abc]3[cd]ef"))
