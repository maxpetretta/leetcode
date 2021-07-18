from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force, O(n^2 log n), O(n)
#         sortedStrs = []
#         groups = []
        
#         for s in strs:
#             sortedStrs.append(sorted(s))
        
#         for i, s in enumerate(strs):
#             indices = [index for index, string in enumerate(sortedStrs) if string == sortedStrs[i]]
            
#             group = []
#             for j in indices:
#                 group.append(strs[j])
            
#             if group not in groups:
#                 groups.append(group)
        
#         return groups


        # Simplified sorted strings, O(nk log k), O(nk)
        # Where n = len(strs) and k = max(len(strs.values))
        # sortedStrs = defaultdict(list)
        # for s in strs:
        #     sortedStrs[tuple(sorted(s))].append(s)
        # return sortedStrs.values()

    
        # Use hash maps, O(nk), O(nk)
        groups = defaultdict(list)
        
        for s in strs:
            map = [0] * 26
            for char in s:
                map[ord(char) - ord('a')] += 1
            groups[tuple(map)].append(s)
        return groups.values()


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))
    print(solver.groupAnagrams(strs=[""]))
    print(solver.groupAnagrams(strs=["a"]))
