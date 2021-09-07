import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort, then keep track of earliest available room, O(n^2 log n), O(n)
        # if not intervals:
        #     return 0
        # intervals.sort()
        # rooms = []
        
        # for interval in intervals:
        #     rooms.sort()
        #     if rooms and rooms[0] <= interval[0]:
        #         rooms[0] = interval[1]
        #     else:
        #         rooms.append(interval[1])
        
        # return len(rooms)
    
        
        # Optimize the above with a priority queue, O(n log n), O(n)
        # if not intervals:
        #     return 0
        
        # intervals.sort()
        # rooms = [intervals[0][1]]
        
        # for interval in intervals[1:]:
        #     if rooms[0] <= interval[0]:
        #         heapq.heappop(rooms)
        #     heapq.heappush(rooms, interval[1])
        
        # return len(rooms)
    
        
        # Split the intervals into separate starts & ends, then use pointers, O(n log n), O(n)
        if not intervals:
            return 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        length = len(intervals)
        rooms, s, e = 0, 0, 0

        while s < length:
            if starts[s] >= ends[e]:
                rooms -= 1
                e += 1
            rooms += 1
            s += 1
        
        return rooms


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))
    print(solver.minMeetingRooms(intervals=[[7,10],[2,4]]))
    print(solver.minMeetingRooms(intervals=[[13,15],[1,13]]))
