# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return
        slow, fast = head.next, head.next.next

        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next

        if fast is None or fast.next is None:
            return

        while slow != head:
            head = head.next
            slow = slow.next

        return slow
