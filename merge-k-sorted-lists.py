from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Brute force, collapse all nodes to list and sort, O(n log n), O(n)
        # nodes = []
        # for l in lists:
        #     while l:
        #         nodes.append(l.val)
        #         l = l.next
        
        # nodes = sorted(nodes)
        # head = prev = ListNode(0)
        
        # for i in nodes:
        #     node = ListNode(i)
        #     prev.next = node
        #     prev = prev.next
        # return head.next
        
        
        # Use two pointer method, O(nk), O(1)
        # def mergeLists(l1, l2):
        #     if l1 is None:
        #         return l2
        #     elif l2 is None:
        #         return l1
        #     elif l2.val < l1.val:
        #         l1, l2 = l2, l1
            
        #     prev, p1, p2 = l1, l1.next, l2
            
        #     while p1 and p2:
        #         if p1.val <= p2.val:
        #             prev.next = p1
        #             p1 = p1.next
        #         else:
        #             prev.next = p2
        #             p2 = p2.next
        #         prev = prev.next
            
        #     prev.next = p1 if p1 else p2
        #     return l1
        
        # k = len(lists)
        # if k == 0:
        #     return None
        # elif k == 1:
        #     return lists[0]
        
        # l1 = lists[0]
        # for i in range(1, k):
        #     l2 = lists[i]
        #     l1 = mergeLists(l1, l2)
        
        # return l1
        
        
        # Adapt two pointer to a mergesort, O(n log k), O(1)
        def mergeLists(l1, l2):
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
            
            prev.next = p1 if p1 else p2
            return l1
        
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        
        while k > 1:
            merged = []
            for i in range(0, k, 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < k else None
                merged.append(mergeLists(l1, l2))
            lists = merged
            k = len(lists)
        
        return lists[0]


# Testcases
# [[1,4,5],[1,3,4],[2,6]]
# []
# [[]]