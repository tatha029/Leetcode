# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        def postorderHelper(tree):
            if not tree:
                return
            postorderHelper(tree.left)
            postorderHelper(tree.right)
            postorder.append(tree.val)
        postorderHelper(root)
        return postorder
