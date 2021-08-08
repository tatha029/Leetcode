# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        negInf = -3 * 10**7 - 1
        maxPath = negInf

        def getMaxGain(tree):
            nonlocal maxPath
            if not tree:
                return 0
            leftGain = max(getMaxGain(tree.left), 0)
            rightGain = max(getMaxGain(tree.right), 0)

            curMaxPath = tree.val + leftGain + rightGain
            maxPath = max(curMaxPath, maxPath)
            return tree.val + max(leftGain, rightGain)

        _ = getMaxGain(root)
        return maxPath
