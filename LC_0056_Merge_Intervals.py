class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        minStart, maxEnd = intervals[0][0], intervals[0][1]
        for interval in intervals:
            if minStart <= interval[0] <= maxEnd: # can't be < minStart since it is sorted
                maxEnd = max(maxEnd, interval[1])
            else:
                merged.append([minStart, maxEnd])
                minStart, maxEnd = interval[0], interval[1]
        merged.append([minStart, maxEnd])
        return merged
