# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(val=0, next=head)
        aheadNode, iterNode = dummy, dummy
        for _ in range(n+1):
            aheadNode = aheadNode.next
        while aheadNode is not None:
            iterNode, aheadNode = iterNode.next, aheadNode.next
        if iterNode.next is None:
            iterNode = iterNode.next
        else:
            iterNode.next = iterNode.next.next
        return dummy.next
