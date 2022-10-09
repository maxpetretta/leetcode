# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use recursion to merge the lists, O(m + n), O(m + n)
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # elif list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        
        
        # Use two pointers to keep track of positions, O(m + n), O(1)
        
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
# [1,2,4], [1,3,4]
# [], []
# [], [0]
# [1], [1]
