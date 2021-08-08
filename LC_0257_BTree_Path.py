# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def binTreePathHelper(tree, path):
            if not tree.left and not tree.right:
                res.append(path)
            if tree.left:
                leftPath = path + '->' + str(tree.left.val)
                binTreePathHelper(tree.left, leftPath)
            if tree.right:
                rightPath = path + '->' + str(tree.right.val)
                binTreePathHelper(tree.right, rightPath)

        res = []
        binTreePathHelper(root,str(root.val))
        return res
