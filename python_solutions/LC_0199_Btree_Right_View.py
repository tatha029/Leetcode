# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        rightView = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, lvl = queue.popleft()
            if not queue or queue[0][1] > lvl:
                # rightmost element in the level
                rightView.append(node.val)
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right, lvl+1))
        return rightView
