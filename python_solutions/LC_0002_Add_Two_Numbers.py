# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = iterNode = ListNode()
        carry = 0
        while l1 is not None and l2 is not None:
            iterNode.next = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10
            l1, l2, iterNode = l1.next, l2.next, iterNode.next
        remList = l1 or l2
        while remList is not None:
            iterNode.next = ListNode((remList.val + carry)%10)
            carry = (remList.val + carry)//10
            remList, iterNode = remList.next, iterNode.next
        if carry > 0:
            iterNode.next = ListNode(carry)
        return head.next
