# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Hash map of previous memory addresses, O(n), O(n)
        # seen = set()
        
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
        
        
        # Two pointer moving at different speeds, O(n), O(1)
        # if not head:
        #     return False
        
        # slow, fast = head, head.next
        # while slow != fast:
        #     if fast is None or fast.next is None:
        #         return False
        #     slow = slow.next
        #     fast = fast.next.next
        # return True
        
        
        # Use dummy node to determine if a cycle exists, O(n), O(1)
        if not head or not head.next:
            return False

        dummy = ListNode(None)        
        previous, current = head, head.next
        
        while current.next:
            previous.next = dummy
            if current.next.val == None:
                return True
            else:
                previous = current
                current = current.next
        return False


# Testcases
# [3,2,0,-4], 1
# [1,2], 0
# [1], -1
