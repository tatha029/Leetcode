class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        for i in s:
            val = val*26 + (ord(i)-64)
        return val
