# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checkNode(tree, curMax):
            if not tree:
                return
            if tree.val >= curMax:
                self.good += 1
                checkNode(tree.left, tree.val)
                checkNode(tree.right, tree.val)
            else:
                checkNode(tree.left, curMax)
                checkNode(tree.right, curMax)

        self.good = 0
        checkNode(root, root.val)
        return self.good
