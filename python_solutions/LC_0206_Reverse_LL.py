# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummyHead = ListNode(next=head)
        startNode, iterNode = head, head.next
        while iterNode is not None:
            dummyHead.next, startNode.next, iterNode.next = startNode.next, iterNode.next, dummyHead.next
            iterNode = startNode.next
        return dummyHead.next
