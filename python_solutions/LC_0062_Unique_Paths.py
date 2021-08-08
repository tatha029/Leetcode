class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # permutation of (m-1) downs and (n-1) rights
        return math.comb(m+n-2, m-1)
