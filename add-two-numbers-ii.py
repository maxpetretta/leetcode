from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the lists, then add the values, O(max(n)), O(max(n))
        # def reverseList(head) -> ListNode:
        #     last = None
        #     while head:
        #         temp, head.next = head.next, last
        #         last, head = head, temp
        #     return last
        
        # carry, head = 0, None
        # l1, l2 = reverseList(l1), reverseList(l2)
        # while l1 or l2:
        #     # Handle empty values
        #     v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
        #     val = v1 + v2 + carry
            
        #     # Add new node to answer
        #     digit, carry = val % 10, val // 10
        #     current = ListNode(digit, head)
            
        #     # Advance lists
        #     head = current
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        
        # # Add an extra node if the carry is non-zero
        # if carry:
        #     current = ListNode(carry, head)
        #     head = current
        # return head
        
    
        """
        Add lists without reversing, ignoring carry until the end
        O(max(n)), O(max(n))
        """
        def lenList(head) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        # Sum the lists, ignoring the carry
        n1, n2 = lenList(l1), lenList(l2)
        curr1, curr2 = l1, l2
        head = None
        
        # Add corresponding positions only
        while n1 and n2:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1
            
            node = ListNode(val)
            node.next, head = head, node
        
        # Take carry into account
        current, head = head, None
        carry = 0
        while current:
            val = current.val + carry
            digit, carry = val % 10, val // 10
            
            node = ListNode(digit)
            node.next, head = head, node
            current = current.next
        
        # Add an extra node if the carry is non-zero
        if carry:
            node = ListNode(carry, head)
            head = node
        return head


# Testcases
# [7,2,4,3], [5,6,4]
# [2,4,3], [5,6,4]
# [0], [0]
