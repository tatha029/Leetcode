from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # base case
        if not prerequisites:
            return True

        degree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        # create graph
        for node in prerequisites:
            parent, child = node[0], node[1]
            graph[parent].append(child)
            degree[child] += 1

        # search
        queue, orderedVertices = deque(), deque()
        for key in degree:
            if degree[key] == 0:
                queue.append(key) # all courses with 0 prereq.

        while queue:
            node = queue.popleft()
            orderedVertices.append(node)
            for vertex in graph[node]:
                degree[vertex] -= 1
                if degree[vertex] == 0: # all prereq of vertex is done
                    queue.append(vertex)

        return len(orderedVertices) == numCourses
