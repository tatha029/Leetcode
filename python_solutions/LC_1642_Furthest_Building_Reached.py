class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prevHeight = heights[0]
        maxHeap = []
        for i in range(len(heights)):
            diff = heights[i] - prevHeight
            if diff > 0:
                bricks -= diff
                heapq.heappush(maxHeap, -diff)
                if bricks < 0:
                    bricks -= heapq.heappop(maxHeap)
                    ladders -= 1
                    if ladders < 0:
                        return i-1
            prevHeight = heights[i]
        return i
