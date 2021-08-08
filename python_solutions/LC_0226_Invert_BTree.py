# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invertTreeHelper(tree):
            if not tree:
                return
            copy = TreeNode(tree.val)
            copy.left = invertTreeHelper(tree.right)
            copy.right = invertTreeHelper(tree.left)
            return copy
        return invertTreeHelper(root)
