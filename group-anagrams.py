from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force, O(n^2 log n), O(n)
        # sortedStrs = []
        # groups = []
        
        # for s in strs:
        #     sortedStrs.append(sorted(s))
        
        # for i, s in enumerate(strs):
        #     indices = [index for index, string in enumerate(sortedStrs) if string == sortedStrs[i]]
            
        #     group = []
        #     for j in indices:
        #         group.append(strs[j])
            
        #     if group not in groups:
        #         groups.append(group)
        
        # return groups


        # Group words using a hashmap of sorted strings, O(nk log k), O(nk)
        # Where n = len(strs) and k = max(len(strs.values))
        # hashmap = defaultdict(list)
        # for word in strs:
        #     hashmap[tuple(sorted(word))].append(word)
        # return hashmap.values()

    
        # Hash the number of each char in the string, O(nk), O(nk)
        answer = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            answer[tuple(count)].append(word)
        return answer.values()


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))
    print(solver.groupAnagrams(strs=[""]))
    print(solver.groupAnagrams(strs=["a"]))
