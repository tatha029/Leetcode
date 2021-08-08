class Solution:
    def myAtoi(self, s: str) -> int:
        def extractNum(s):
            i, x = 0, '0'
            if s[0] == '-':
                sgn = -1
                i += 1
            elif s[0] == '+':
                sgn = 1
                i += 1
            else:
                sgn = 1
            while i < len(s) and s[i] in '1234567890':
                x += s[i]
                i += 1
            return sgn * int(x)

        j = 0
        while j < len(s) and s[j] == ' ':
            j += 1

        if j < len(s):
            if s[j] in '+-1234567890':
                val = extractNum(s[j:])
            else:
                val = 0
        else:
            val = 0
        if val >= 2**31:
            val = 2**31 - 1
        elif val < -2**31:
            val = -2**31
        return val
