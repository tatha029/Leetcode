class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour = {}
        for vertex in range(len(graph)):
            if vertex not in colour:
                colour[vertex] = 0
                stack = [vertex]
                while stack:
                    vertex = stack.pop()
                    for nei in graph[vertex]:
                        if nei not in colour:
                            colour[nei] = colour[vertex]^1
                            stack.append(nei)
                        else:
                            if colour[nei] == colour[vertex]:
                                return False
        return True
