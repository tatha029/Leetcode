class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquaresDigits(x):
            t = 0
            while x > 0:
                t += (x%10)**2
                x //= 10
            return t
        visited = {}
        while n not in visited:
            if n == 1:
                return True
            else:
                visited[n] = 1
                n = sumSquaresDigits(n)
        return False
