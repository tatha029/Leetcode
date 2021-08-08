class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = {0:1, 1:1}
        def climbStairsHelper(n):
            if n in num_steps:
                return num_steps[n]
            else:
                num_steps[n] = climbStairsHelper(n-1) + climbStairsHelper(n-2)
                return num_steps[n]
        return climbStairsHelper(n)
