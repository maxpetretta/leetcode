class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Brute force loop over s, removing any k sequences, O(n^2 / k), O(1)
        # i, n = 0, len(s) - k + 1
        # while i < n:
        #     if len(set(s[i:i + k])) == 1:
        #         s = s[:i] + s[i + k:]
        #         i, n = 0, len(s) - k + 1
        #         continue
        #     i += 1
        # return s
                
        
        # Use a stack to track character counts, O(n), O(n)
        stack = [] # Holds [char, count]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join(char * count for char, count in stack)


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.removeDuplicates(s="abcd", k=2))
    print(solver.removeDuplicates(s="deeedbbcccbdaa", k=3))
    print(solver.removeDuplicates(s="pbbcggttciiippooaais", k=2))
    print(solver.removeDuplicates(s="nnwssswwnvbnnnbbqhhbbbhmmmlllm", k=3))
    print(solver.removeDuplicates(s="yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k=4))
