# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeHelper(preorder_idx, inorder_start, inorder_end):
            if inorder_start >= inorder_end:
                # no tree node available
                return None, preorder_idx
            tree = TreeNode(val=preorder[preorder_idx])
            inorder_idx = inorder.index(preorder[preorder_idx])
            preorder_idx += 1
            tree.left, preorder_idx = buildTreeHelper(preorder_idx, inorder_start, inorder_idx)
            tree.right, preorder_idx = buildTreeHelper(preorder_idx, inorder_idx+1, inorder_end)
            return tree, preorder_idx
        return buildTreeHelper(0, 0, len(inorder))[0]
