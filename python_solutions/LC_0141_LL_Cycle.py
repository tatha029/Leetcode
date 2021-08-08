# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        x, y = head, head
        while x is not None and y is not None and y.next is not None:
            x, y = x.next, y.next.next
            if x == y:
                return True
        return False
