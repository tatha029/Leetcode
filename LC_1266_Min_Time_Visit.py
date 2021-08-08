class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        start = points[0]
        time = 0
        for end in points:
            r, c = abs(end[0]-start[0]), abs(end[1]-start[1])
            time += max(r,c)
            start = end
        return time
