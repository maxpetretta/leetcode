from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute force compare every character up to min string length, O(m * n), O(1)
        # length, answer = len(strs[0]), ""
        
        # for i in range(length):
        #     char = strs[0][i]
        #     for s in strs[1:]:
        #         if s[i] != char:
        #             return answer
        #     answer += char
        # return answer

        
        """
        Use binary search to discard extra characters
        O(s log m) where s = sum of all characters & m = minimum string length, O(1)
        """
        def isCommonPrefix(strs, mid):
            prefix = strs[0][:mid]
            for s in strs[1:]:
                if not s.startswith(prefix):
                    return False
            return True
                
        left, right = 0, min([len(s) for s in strs])
        while left <= right:
            mid = (left + right) // 2
            if isCommonPrefix(strs, mid):
                left = mid + 1
            else:
                right = mid - 1
        index = (left + right) // 2
        return strs[0][:index]


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.longestCommonPrefix(strs=["flower","flow","flight"]))
    print(solver.longestCommonPrefix(strs=["dog","racecar","car"]))
    print(solver.longestCommonPrefix(strs=["reflower","flow","flight"]))
