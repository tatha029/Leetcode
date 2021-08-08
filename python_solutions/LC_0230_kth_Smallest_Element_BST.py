# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        traversal = []
        def inorder(tree):
            if not tree:
                return
            inorder(tree.left)
            traversal.append(tree.val)
            inorder(tree.right)
        inorder(root)
        return traversal[k-1]
