class Solution:
    def numSquares(self, n: int) -> int:
        mem = [float(inf)]*n
        for i in range(n):
            x = 1
            while x*x <= i+1:
                if x*x == i+1:
                    mem[i] = 1
                else:
                    mem[i] = min(mem[i], 1 + mem[i-x*x])
                x += 1
        return mem[-1]
