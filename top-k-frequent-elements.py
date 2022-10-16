from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sort hashmap of occurrences with a heap, O(n log k) if k < n else O(n log n), O(n + k)
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        # return heapq.nlargest(k, count.keys(), key=count.get)
    
        
        # Use quickselect algorithm, average O(n) worst-case O(n^2), O(n)
        # count = Counter(nums)
        # keys = list(count.keys())
        
        # def partition(left, right, pivot) -> int:
        #     frequency = count[keys[pivot]]
        #     # Move pivot to end
        #     keys[pivot], keys[right] = keys[right], keys[pivot]
            
        #     # Move less frequent keys to the left
        #     store = left
        #     for i in range(left, right):
        #         if count[keys[i]] < frequency:
        #             keys[store], keys[i] = keys[i], keys[store]
        #             store += 1
            
        #     # Move pivot to final place
        #     keys[right], keys[store] = keys[store], keys[right]
        #     return store
        
        # def quickselect(left, right, smallest) -> None:
        #     if left == right:
        #         return
            
        #     pivot = random.randint(left, right)
        #     pivot = partition(left, right, pivot)
            
        #     # If the pivot is in the final position
        #     if smallest == pivot:
        #         return
            
        #     # Move left
        #     elif smallest < pivot:
        #         quickselect(left, pivot - 1, smallest)
            
        #     # Move right
        #     else:
        #         quickselect(pivot + 1, right, smallest)
        
        # n = len(keys)
        # quickselect(0, n - 1, n - k)
        # return keys[n - k:]


        # Use bucketsort algorithm, O(n), O(n)
        count = Counter(nums)
        frequency = [[] for i in range(len(nums) + 1)]
        
        for n, c in count.items():
            frequency[c].append(n)
        
        answer = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
        
# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.topKFrequent(nums=[1,1,1,2,2,3], k=2))
    print(solver.topKFrequent(nums=[1], k=1))
    print(solver.topKFrequent(nums=[3,0,1,0], k=1))
