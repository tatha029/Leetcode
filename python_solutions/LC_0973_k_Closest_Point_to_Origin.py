class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                # it can be atmost k+1; hence O(k) space
                # inserting all to heap and getting n_smallest will take O(n) space
                heapq.heappop(heap)
        return [i for _,i in heap]
