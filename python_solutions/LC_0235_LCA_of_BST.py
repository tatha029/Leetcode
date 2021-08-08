# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcaHelper(tree):
            if tree.val >= p.val and tree.val <= q.val:
                return tree
            if tree.val > p.val and tree.val > q.val:
                return lcaHelper(tree.left)
            else:
                return lcaHelper(tree.right)

        if p.val > q.val:
            p, q = q, p
        return lcaHelper(root)
