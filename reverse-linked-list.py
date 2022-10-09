# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Reorder while iterating over the list, O(n), O(1)
        # previous, current = None, head
        
        # while current:
        #     temp = current.next
        #     current.next = previous
        #     previous = current
        #     current = temp
        # return previous

        # Reorder the list recursively, O(n), O(n)
        if not head or not head.next:
            return head
            
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


# Testcases
# [1,2,3,4,5]
# [1,2]
# []
