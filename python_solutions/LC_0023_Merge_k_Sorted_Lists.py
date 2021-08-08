# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        head = iterNode = ListNode()
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)

        while heap:
            node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, node.next)
            iterNode.next = node
            iterNode = iterNode.next
        return head.next
