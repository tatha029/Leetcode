# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead = ListNode()
        dummyHead.next = head
        iterNode = dummyHead
        while iterNode.next:
            if iterNode.next.val == val:
                iterNode.next = iterNode.next.next
            else:
                iterNode = iterNode.next
        return dummyHead.next
