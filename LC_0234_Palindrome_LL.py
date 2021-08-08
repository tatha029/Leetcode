# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def lengthLL(node):
            l = 0
            while node is not None:
                l += 1
                node = node.next
            return l

        l = lengthLL(head)
        if l < 2:
            return True

        # invert the 2nd half of the array
        sublistHead = ListNode(next=head)
        for _ in range(l//2 + l%2):
            sublistHead = sublistHead.next
        startNode, iterNode = sublistHead.next, sublistHead.next.next
        while iterNode is not None:
            sublistHead.next, startNode.next, iterNode.next = startNode.next, iterNode.next, sublistHead.next
            iterNode = startNode.next

        # once inverted, check the palindrone via 2 pointers
        slow, fast = head, head
        for _ in range(l//2 + l%2):
            fast = fast.next
        while fast is not None:
            if slow.val != fast.val:
                return False
            else:
                slow, fast = slow.next, fast.next
        return True
