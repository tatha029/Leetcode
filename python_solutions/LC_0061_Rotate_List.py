# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        n, iterNode = 0, head
        tail, kthNodeFromEnd = None, None
        while iterNode is not None:
            n += 1
            if iterNode.next is None:
                tail = iterNode
            iterNode = iterNode.next

        iterNode = head
        k %= n
        if k == 0:
            return head

        for i in range(n-k-1):
            iterNode = iterNode.next
        kthNodeFromLast = iterNode

        head, kthNodeFromLast.next, tail.next = kthNodeFromLast.next, None, head

        return head
