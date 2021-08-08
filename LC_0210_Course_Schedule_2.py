class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # base case
        if not prerequisites:
            return range(numCourses)

        degree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        # create graph
        for node in prerequisites:
            parent, child = node[1], node[0]
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

        if len(orderedVertices) == numCourses:
            return list(orderedVertices)
