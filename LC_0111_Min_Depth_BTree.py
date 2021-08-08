# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root,1))
        while queue:
            tree, depth = queue.popleft()
            if tree.left:
                queue.append((tree.left, depth+1))
            if tree.right:
                queue.append((tree.right, depth+1))
            if not tree.left and not tree.right:
                return depth
