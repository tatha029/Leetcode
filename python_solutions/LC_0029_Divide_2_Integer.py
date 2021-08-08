class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quo, temp = 0, 0
        sgn = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        for i in reversed(range(32)):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quo |= 1 << i
        if -2**31 <= sgn*quo < 2**31:
            return sgn*quo
        else:
            return 2**31 - 1
