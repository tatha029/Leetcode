# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def findHeight(tree):
            if not tree:
                return (0, True)
            left = findHeight(tree.left)
            right = findHeight(tree.right)

            if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
                return (max(left[0], right[0])+1, True)
            else:
                return (0, False)
        return findHeight(root)[1]
