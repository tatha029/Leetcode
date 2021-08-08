# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        iterNode = head
        while iterNode.next:
            if iterNode.next.val == iterNode.val:
                iterNode.next = iterNode.next.next
            else:
                iterNode = iterNode.next
        return head
