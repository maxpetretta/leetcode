# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find length on first pass, remove node on second, O(length), O(1)
        # length = 0
        
        # node = head
        # while node:
        #     length += 1
        #     node = node.next
        
        # if length-n-1 == -1:
        #     return head.next
        
        # node = head
        # for i in range(length):
        #     if i == length - n - 1:
        #         node.next = node.next.next
        #         break
        #     node = node.next
        
        # return head
        
    
        # Use two pointers spaced n+1 nodes apart, O(length), O(1)
        count = 0
        ptr = node = head
        
        while node:
            if node.next is None and count == n:
                ptr.next = ptr.next.next
                return head
            elif count == n:
                node = node.next
                ptr = ptr.next
            else:
                node = node.next
                count += 1
            
        return head.next if count == n else head


# Testcases
# [1,2,3,4,5], 2
# [1], 1
# [1,2], 1
# [1,2], 2
