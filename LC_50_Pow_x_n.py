class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x

        ans, powX = 1, x
        while n > 0:
            if n % 2 == 1:
                ans *= powX
            powX *= powX
            n = n//2
        return ans
