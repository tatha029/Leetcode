class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        left, right = [], []

        # fill lefts
        stack = []
        for i in range(l):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left.append(0)
            else:
                left.append(stack[-1] + 1)
            stack.append(i)

        # fill rights
        stack = []
        for i in reversed(range(l)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right.append(l-1)
            else:
                right.append(stack[-1] - 1)
            stack.append(i)

        return max([h*(r-l+1) for h,l,r in zip(heights, left, reversed(right))])
