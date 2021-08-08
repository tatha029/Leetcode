# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def inorder(tree):
            nonlocal state
            nonlocal ans
            if not tree:
                return
            inorder(tree.left)
            if state == 0:
                if tree.val == low:
                    state = 1
                    #ans.append(tree.val)
            if state == 1:
                ans += tree.val
                if tree.val == high:
                    state = 0
            inorder(tree.right)

        state, ans = 0, 0
        inorder(root)
        return ans
