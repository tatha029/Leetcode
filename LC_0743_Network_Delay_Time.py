import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        # Dijkstra's algorithm
        inf = n*100 + 1 # w_i <= 100
        dist = {node:inf for node in range(1, n+1)}
        seen = [False]*(n+1)
        dist[k] = 0

        while True:
            candNode, candDist = -1, inf
            """
            Below can be implemented via a heap wherein you pop the smallest distance
            vertex and update its neighbors
            """
            for i in range(1, n+1):
                # in first iter, this will set candNode = k and candDist = 0
                # next iter onwards, it goes to the next unvisited vertex ..
                # .. which can be moved in least distance
                if not seen[i] and dist[i] < candDist:
                    candDist = dist[i]
                    candNode = i

            if candNode < 0:
                # if candNode = -1. then none of the further nodes ..
                # .. can be reached from visited ones
                break
            seen[candNode] = True
            for nei, d in graph[candNode]:
                # update all adjacent vertices with the minimum distance path
                dist[nei] = min(dist[nei], dist[candNode] + d)

        ans = max(dist.values())
        return ans if ans < inf else -1
