# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB, A_iter, B_iter = 0, 0, headA, headB
        while A_iter is not None:
            lenA += 1
            A_iter = A_iter.next
        while B_iter is not None:
            lenB += 1
            B_iter = B_iter.next
        min_len = min(lenA, lenB)
        A_iter, B_iter = headA, headB
        for _ in range(lenA - min_len):
            A_iter = A_iter.next
        for _ in range(lenB - min_len):
            B_iter = B_iter.next

        while A_iter is not None:
            if A_iter == B_iter:
                return A_iter
            else:
                A_iter, B_iter = A_iter.next, B_iter.next
        return None
