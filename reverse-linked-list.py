# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Use recursion, O(n), O(n)
        # def reverse(node):
        #     if not node or not node.next:
        #         return node
        #     head = reverse(node.next)
        #     node.next.next = node
        #     node.next = None
        #     return head
        
        # return reverse(head)
        
        
        # Use iteration, O(n), O(1)
        previous, current = None, head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous


# Testcases
if __name__ == "__main__":
    solver = Solution()
    print(solver.reverseList(head=[1,2,3,4,5]))
    print(solver.reverseList(head=[1,2]))
    print(solver.reverseList(head=[]))