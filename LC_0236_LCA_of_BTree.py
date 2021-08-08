# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcaHelper(tree, p, q):
            if not tree:
                return None
            if tree == p:
                cur = p
            elif tree == q:
                cur = q
            else:
                cur = None
            left = lcaHelper(tree.left, p, q)
            right = lcaHelper(tree.right, p, q)
            ctr = 0
            for x in [left, right, cur]:
                if x is not None:
                    ctr += 1
            if ctr == 0:
                return None
            if ctr == 1:
                return cur or left or right
            if ctr == 2:
                return cur or tree
        return lcaHelper(root, p, q)
