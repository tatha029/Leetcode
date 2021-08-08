import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create graph and sort the destinations
        graph = collections.defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        for _, dest in graph.items():
            dest.sort()
        # dfs
        ans = []
        stack = ['JFK']
        while stack:
            top = stack[-1]
            if not graph[top]: # it must be visited last since it can't go anywhere now
                ans.append(top)
                stack.pop()
            else:
                stack.append(graph[top][0]) # append the first city that can be visited via top
                del graph[top][0]
        return reversed(ans) # ans to be traversed in reverse
