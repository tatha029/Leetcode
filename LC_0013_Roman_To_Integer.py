class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        vals, negs = 0, 0
        for i in range(len(s)):
            vals += roman_num[s[i]]
        for i in range(len(s)-1):
            if s[i] == 'I' and s[i+1] in ['V', 'X']:
                negs += 2
            elif s[i] == 'X' and s[i+1] in ['L', 'C']:
                negs += 20
            elif s[i] == 'C' and s[i+1] in ['D', 'M']:
                negs += 200
        return vals - negs
