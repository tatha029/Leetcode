class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        soe = [0, 0] + [1]*(n-1)
        for i in range(2, int(n**0.5)+1):
            if soe[i] == 1:
                for j in range(2*i, n+1, i):
                    soe[j] = 0
            else:
                continue
        return sum(soe[:n])
