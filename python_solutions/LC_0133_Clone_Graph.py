"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = {}
        queue = deque()
        queue.append(node)
        visited[node.val] = Node(node.val)

        while queue:
            vertex = queue.popleft()
            for nbr in vertex.neighbors:
                if nbr.val not in visited:
                    queue.append(nbr)
                    visited[nbr.val] = Node(nbr.val)
                visited[vertex.val].neighbors.append(visited[nbr.val])

        return visited[node.val]
