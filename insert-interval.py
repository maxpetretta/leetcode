from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Greedy algorithm, merge overlapping intervals, O(n), O(n)
        # start, end = newInterval[0], newInterval[1]
        # curr, length = 0, len(intervals)
        # merged = []
        
        # while curr < length and start > intervals[curr][0]:
        #     merged.append(intervals[curr])
        #     curr += 1
        
        # if not merged or start > merged[-1][1]:
        #     merged.append(newInterval)
        # else:
        #     merged[-1][1] = max(end, merged[-1][1])
        
        # while curr < length:
        #     interval = intervals[curr]
        #     curr += 1
            
        #     if interval[0] > merged[-1][1]:
        #         merged.append(interval)
        #     else:
        #         merged[-1][1] = max(interval[1], merged[-1][1])
        
        # return merged
        
        
        # Simplify the above, O(n), O(n)
        merged = []
        
        for i in range(len(intervals)):
            start, end = newInterval[0], newInterval[1]
            
            if end < intervals[i][0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            elif start > intervals[i][1]:
                merged.append(intervals[i])
            else:
                newInterval = [min(start, intervals[i][0]), max(end, intervals[i][1])]
        
        merged.append(newInterval)
        return merged


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.insert(intervals=[[1,3],[6,9]], newInterval=[2,5]))
    print(solver.insert(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8]))
    print(solver.insert(intervals=[], newInterval=[5,7]))
    print(solver.insert(intervals=[[1,5]], newInterval=[2,3]))
    print(solver.insert(intervals=[[1,5]], newInterval=[2,7]))
