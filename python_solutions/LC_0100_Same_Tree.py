# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def equals(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            return p1.val == p2.val and equals(p1.left, p2.left) and equals(p1.right, p2.right)

        return equals(p, q)
