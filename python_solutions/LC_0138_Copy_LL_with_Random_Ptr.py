"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dummyHead = Node(0)
        iterNode, copyIter, i = head, dummyHead, 0
        nodeArr, hashMap = [], {}
        # copy LL without the random
        while iterNode:
            node = Node(iterNode.val, next=iterNode.next)
            nodeArr.append(node)
            hashMap[iterNode] = i
            i += 1
            copyIter.next = node
            iterNode, copyIter = iterNode.next, copyIter.next

        iterNode, copyIter = head, dummyHead.next
        # assign random
        while iterNode:
            if not iterNode.random:
                copyIter.random = None
            else:
                copyIter.random = nodeArr[hashMap[iterNode.random]]
            iterNode, copyIter = iterNode.next, copyIter.next
        return dummyHead.next
