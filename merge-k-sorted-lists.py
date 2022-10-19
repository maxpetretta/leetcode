
import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute force, collapse all nodes to one list and sort, O(n log n), O(n)
#         nodes = []
#         for l in lists:
#             while l:
#                 nodes.append(l.val)
#                 l = l.next
        
#         head = node = ListNode(0)
#         for val in sorted(nodes):
#             node.next = ListNode(val)
#             node = node.next
#         return head.next
    
        """
        Merge each list individually using two pointers
        O(kn) where k is number of lists and n is maximum number of nodes, O(1)
        """        
        # length = len(lists)
        # list1 = lists[0]
        # for i in range(1, length):
        #     list2 = lists[i]
        #     list1 = self.mergeTwoLists(list1, list2)
        # return list1
        
        
        # Adapt two pointers to a mergesort, O(n log k), O(1)
#         length = len(lists)
#         if length == 0:
#             return None
#         elif length == 1:
#             return lists[0]
        
#         while length > 1:
#             merged = []
#             for i in range(0, length, 2):
#                 list1 = lists[i]
#                 list2 = lists[i + 1] if (i + 1) < length else None
#                 merged.append(self.mergeTwoLists(list1, list2))
#             lists, length = merged, len(merged)
#         return lists[0]


        # Add every node to a heap, then build a sorted list, O(n log k), O(n)
        head = curr = ListNode(0)
        length, heap = len(lists), []
        
        for i in range(length):
            while lists[i]:
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        
        while heap:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
        return head.next
    

    """
    Solution from merge 2 sorted lists, component of above solutions 
    Use two pointers to keep track of positions, O(m + n), O(1)
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty lists
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        # Place lowest value as list1
        elif list2.val < list1.val:
            list1, list2 = list2, list1
        
        prev, p1, p2 = list1, list1.next, list2
        while p1 and p2:
            if p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
            elif p2.val < p1.val:
                prev.next = p2
                p2 = p2.next
            prev = prev.next
        
        # Connect the last node
        prev.next = p1 if p1 else p2
        
        return list1


# Testcases
# [[1,4,5],[1,3,4],[2,6]]
# []
# [[]]
