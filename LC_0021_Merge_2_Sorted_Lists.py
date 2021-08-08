# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = iterNode = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                iterNode.next = l1
                iterNode, l1 = iterNode.next, l1.next
            else:
                iterNode.next = l2
                iterNode, l2 = iterNode.next, l2.next
        iterNode.next = l1 or l2
        return headNode.next
