# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Brute force, find last node at each position, O(n^2 - ni), O(1)
        # node = head
        # if node.next is None:
        #     return
        
        # while node.next.next:
        #     ptr = node
        #     after = node.next
            
        #     while ptr.next:
        #         curr = ptr.next
        #         if curr.next is None:
        #             node.next = curr
        #             node.next.next = after
        #             ptr.next = None
        #             break
        #         ptr = ptr.next
            
        #     node = after
        #     if node.next is None:
        #         return
        
        
        # Use two pointers, reverse second half, O(n), O(1)
        
        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge lists together
        first, second = head, prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
        
# Testcases
# [1,2,3,4]
# [1,2,3,4,5]
# [1]
