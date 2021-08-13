# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        def preorderHelper(tree):
            if not tree:
                return
            preorder.append(tree.val)
            preorderHelper(tree.left)
            preorderHelper(tree.right)
        preorderHelper(root)
        return preorder
