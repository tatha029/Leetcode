# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(left, right):
            if left is None and right is None:
                return True
            # above handles the case when both are None so only one is None is captured below
            if left is None or right is None:
                return False
            return left.val == right.val and isSame(left.left, right.right) and isSame(left.right, right.left)
        if root is None:
            return True
        return isSame(root.left, root.right)
