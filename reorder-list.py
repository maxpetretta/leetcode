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
        # For each odd numbered node, cast ahead to get the last node, O(n^2 - ni), O(1)
        # node = head
        # if node.next is None:
        #     return
        
        # while node.next.next:
        #     ptr, after = node, node.next
            
        #     # Move ptr to second to last position
        #     while ptr.next.next:
        #         ptr = ptr.next

        #     # Move last node to front of list
        #     last, ptr.next = ptr.next, None
        #     node.next, last.next = last, after
            
        #     # Update the current node
        #     node = node.next.next
        
        
        # Merge the first half of list with a reversed second half, O(n), O(1)
        
        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        
        # Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        
# Testcases
# [1,2,3,4]
# [1,2,3,4,5]
# [1]
