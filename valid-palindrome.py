class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute force using a stack, O(n), O(n)
        # s = ''.join(char for char in s if char.isalnum()).lower()
        # length = len(s)
        # stack = []
        
        # for i in range(length//2):
        #     stack.append(s[i])
        
        # mid = (length // 2) if length % 2 == 0 else (length // 2) + 1
        # for i in range(mid, length):
        #     if stack[-1] == s[i]:
        #         stack.pop()
        #     else:
        #         return False
        
        # return stack == []
    
    
        # Compare s with it's reverse, O(n), O(n)
        # s = ''.join(char for char in s if char.isalnum()).lower()
        # return s == s[::-1]
             
    
        # Read from both ends using two pointers, O(n), O(1)
        s = ''.join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solver.isPalindrome(s="race a car"))
