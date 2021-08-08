class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x *= sign
        rev = 0
        while x > 0:
            rev = rev*10 + x%10
            x //= 10
        if -1* 2**31 <= rev < 2**31:
            return sign*rev
        return 0
