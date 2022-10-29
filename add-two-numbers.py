from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate over the list, summing the nodes in place, O(max(n)), O(max(n))
        carry = 0
        head = current = ListNode()
        while l1 or l2 or carry:
            # Handle empty values
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            val = v1 + v2 + carry
            
            # Add new node to answer
            digit, carry = val % 10, val // 10
            current.next = ListNode(digit)

            # Advance lists
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


# Testcases
# [2,4,3], [5,6,4]
# [0], [0]
# [9,9,9,9,9,9,9], [9,9,9,9]
