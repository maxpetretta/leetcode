from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy algorithm, always remove interval with larger end, O(n log n), O(1)
        # intervals.sort()
        # prev = intervals[0]
        # removed = 0
        
        # for interval in intervals[1:]:
        #     if interval[0] < prev[1]:
        #         if prev[1] > interval[1]:
        #             prev = interval
        #         removed += 1
        #     else:
        #         prev = interval
        # return removed
    
    
        # Simplify the above, by sorting based on ends, O(n log n), O(1)
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        removed = 0
        
        for interval in intervals[1:]:
            if interval[0] < prev[1]:
                removed += 1
            else:
                prev = interval
        return removed
                    

# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.eraseOverlapIntervals(intervals=[[1,2],[2,3],[3,4],[1,3]]))
    print(solver.eraseOverlapIntervals(intervals=[[1,2],[1,2],[1,2]]))
    print(solver.eraseOverlapIntervals(intervals=[[1,2],[2,3]]))
    print(solver.eraseOverlapIntervals(intervals=[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
