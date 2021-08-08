# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def toBSTHelper(low, high):
            if low > high:
                return None
            mid = (low+high)//2
            node = TreeNode(nums[mid])
            node.left = toBSTHelper(low, mid-1)
            node.right = toBSTHelper(mid+1, high)
            return node
        return toBSTHelper(0, len(nums)-1)
