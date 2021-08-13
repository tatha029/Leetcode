# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        sol, levelSol = [], []
        cur_lvl = 0
        queue.append((root, 0))
        if not root:
            return []
        while len(queue) > 0:
            node, lvl = queue.popleft()
            if node.left:
                queue.append((node.left, lvl+1))
            if node.right:
                queue.append((node.right, lvl+1))
            if lvl == cur_lvl:
                levelSol.append(node.val)
            else:
                sol.append(levelSol)
                levelSol = [node.val]
                cur_lvl += 1
        sol.append(levelSol)
        return reversed(sol)
