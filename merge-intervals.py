from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort then merge, O(n log n), O(n)
        def merge(curr, next):
            new = [min(curr[0], next[0]), max(curr[1], next[1])]
            return new
        
        intervals = sorted(intervals)
        merged = [intervals.pop(0)]
        
        while intervals:
            curr = merged[-1]
            next = intervals.pop(0)
    
            if curr[1] >= next[0]:
                merged.pop()
                merged.append(merge(curr, next))
            else:
                merged.append(next)
        
        return merged


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))
    print(solver.merge(intervals=[[1,4],[4,5]]))
    print(solver.merge(intervals=[[1,4],[0,0]]))
    print(solver.merge(intervals=[[1,4],[0,2],[3,5]]))
