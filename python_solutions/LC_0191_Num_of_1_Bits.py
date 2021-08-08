class Solution:
    def hammingWeight(self, n: int) -> int:
        wt = 0
        while n > 0:
            wt += n & 1
            n = n >> 1
        return wt
