class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # maxWidth * maxHeight
        maxWidth, maxHeight = 0, 0
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        for i in range(1, len(horizontalCuts)):
            maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i-1])

        for i in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i-1])

        return (maxHeight * maxWidth) % (10**9 + 7)
