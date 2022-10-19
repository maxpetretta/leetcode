# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find length on first pass, remove node on second, O(length), O(1)
        # node, length = head, 0
        # while node:
        #     length += 1
        #     node = node.next
        
        # if (length - n - 1) == -1:
        #     return head.next
        
        # node = head
        # for i in range(length):
        #     if i == (length - n - 1):
        #         node.next = node.next.next
        #         break
        #     node = node.next
        # return head
        
    
        # Use two pointers spaced n + 1 nodes apart, O(length), O(1)
        start = ListNode(0, head)
        slow, fast = start, head
        
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        return start.next


# Testcases
# [1,2,3,4,5], 2
# [1], 1
# [1,2], 1
# [1,2], 2
