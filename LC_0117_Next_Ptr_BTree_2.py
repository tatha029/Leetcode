"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs soln: if depth == queue[0][1], then tree.next = queue[0][0] else None

        def findNext(tree):
            # given parent tree, find the next node for one of the children
            # return priority : left -> right -> next's children -> None
            while tree:
                if tree.left:
                    return tree.left
                if tree.right:
                    return tree.right
                tree = tree.next
            return tree

        def connectHelper(tree):
            # tree here is the parent tree node
            if not tree or (not tree.left and not tree.right):
                # if it's a null tree or a leaf
                return tree
            needLink = None # which subtree needs to get the link via findNext
            if tree.left and not tree.right:
                # if it has only left subtree
                needLink = tree.left
            elif not tree.left and tree.right:
                # if it has only right subtree
                needLink = tree.right
            else:
                # if it has both, left.next = right
                tree.left.next = tree.right
                needLink = tree.right
            needLink.next = findNext(tree.next)
            connectHelper(tree.right)
            connectHelper(tree.left)
            return tree

        return connectHelper(root)
