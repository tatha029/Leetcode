class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        leftBound, rightBound = [0], [0]
        # find left boundaries
        max_till_now = 0
        for i in range(len(height)):
            if height[i] > max_till_now:
                max_till_now = height[i]
            leftBound.append(max_till_now)
        # find right boundaries
        max_till_now = 0
        for i in reversed(range(len(height))):
            if height[i] > max_till_now:
                max_till_now = height[i]
            rightBound.append(max_till_now)
        # calculate water trapped
        trapWater = sum([max(min(x,y)-z,0) for x,y,z in zip(leftBound, reversed(rightBound), height)])
        return trapWater
