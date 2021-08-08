class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        largeNum = 2**32
        return largeNum % n == 0
