"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        queue, visited = deque(), set()
        totImp = 0

        queue.append(emap[id])

        while queue:
            top = queue.popleft()
            visited.add(top.id)
            totImp += top.importance
            for s in top.subordinates:
                if emap[s].id not in visited:
                    queue.append(emap[s])
        return totImp
