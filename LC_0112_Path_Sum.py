# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def hasPartialSum(tree, partialSum):
            if not tree.left and not tree.right:
                return partialSum == tree.val
            left, right = False, False
            if tree.left:
                left = hasPartialSum(tree.left, partialSum - tree.val)
            if tree.right:
                right = hasPartialSum(tree.right, partialSum - tree.val)
            return left or right

        if not root:
            return False

        return hasPartialSum(root, targetSum)
