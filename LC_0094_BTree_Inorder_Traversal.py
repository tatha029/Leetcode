# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        def inorderHelper(tree):
            if not tree:
                return
            inorderHelper(tree.left)
            inorder.append(tree.val)
            inorderHelper(tree.right)
        inorderHelper(root)
        return inorder
