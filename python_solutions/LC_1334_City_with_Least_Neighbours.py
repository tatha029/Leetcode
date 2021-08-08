import collections
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # generate the least distance matrix
        inf = n * 10**4 + 1 # edge weight <= 10**4
        least_dist = [[inf for _ in range(n)] for _ in range(n)]
        for u,v,w in edges:
            least_dist[u][v] = w
            least_dist[v][u] = w
        for i in range(n):
            least_dist[i][i] = 0

        # update the least distances as dist(u,v) = min(dist(u,i)+dist(i,v))
        for inter in range(n):
            for start in range(n):
                for end in range(n):
                    least_dist[start][end] = min(least_dist[start][end],\
                                                 least_dist[start][inter]+least_dist[inter][end])

        # find threshold distance adjacent vertices for all vertices
        neighbours = {}
        leastNbr, least = 0, n
        for start in range(n):
            neighbours[start] = 0
            for end in range(n):
                if least_dist[start][end] <= distanceThreshold:
                    neighbours[start] += 1
            if neighbours[start] <= least:
                leastNbr, least = start, neighbours[start]
        return leastNbr
