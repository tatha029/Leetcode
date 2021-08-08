from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        inf = 10**4 + 1 # if we encounter x_i = x_j
        l = len(points)
        slopes = [0 for _ in range(l)]
        maxSameSlopes = 0

        for s in range(l):
            for t in range(l):
                if s == t:
                    slopes[t] = inf + 1
                    continue
                dx, dy = points[s][0] - points[t][0], points[s][1] - points[t][1]
                slopes[t] = dy/dx if dx != 0 else inf
            ctr = Counter(slopes)
            maxSameSlopes = max(maxSameSlopes, ctr[max(slopes, key=slopes.count)])

        return maxSameSlopes+1
