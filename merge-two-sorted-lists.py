# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Use recursion, O(m + n), O(m + n)
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        
        
        # Use two pointers, O(m + n), O(1)
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l2.val < l1.val:
            l1, l2 = l2, l1
        
        prev, p1, p2 = l1, l1.next, l2
        
        while p1 and p2:
            if p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
            prev = prev.next
        
        # Connect last node
        prev.next = p1 if p1 else p2
        
        return l1


# Testcases
# [1,2,4], [1,3,4]
# [], []
# [], [0]
# [1], [1]
