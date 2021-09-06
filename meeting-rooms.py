from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Brute force, O(n^2), O(1)
        # if not intervals:
        #     return True
        # length = len(intervals)
        
        # for i in range(length):
        #     for j in range(i+1, length):
        #         # If the later start time occurs before the earlier end time
        #         if max(intervals[i][0], intervals[j][0]) < min(intervals[i][1], intervals[j][1]):
        #             return False
        # return True
                
        
        # Sort the list by start, O(n log n), O(1)
        if not intervals:
            return True
        intervals.sort()
        prev = intervals[0][1]
        
        for curr in intervals[1:]:
            if curr[0] < prev:
                return False
            else:
                prev = curr[1]
        return True


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.canAttendMeetings(intervals=[[0,30],[5,10],[15,20]]))
    print(solver.canAttendMeetings(intervals=[[7,10],[2,4]]))
    print(solver.canAttendMeetings(intervals=[[0,30],[60,240],[90,120]]))
