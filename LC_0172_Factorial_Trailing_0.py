class Solution:
    def trailingZeroes(self, n: int) -> int:
        t = 0
        while n > 0:
            t += n//5
            n //=5
        return t
