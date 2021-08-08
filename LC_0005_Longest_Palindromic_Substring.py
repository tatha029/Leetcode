class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCentre(left, right):
            L, R = left, right
            while L>=0 and R<len(s) and s[L]==s[R]:
                L -= 1
                R += 1
            return R-L-1

        start = end = 0
        for i in range(len(s)):
            len1 = expandAroundCentre(i, i)
            len2 = expandAroundCentre(i, i+1)
            leng = max(len1, len2)
            if leng > end - start:
                start = i - (leng-1)//2
                end = i + (leng//2)

        return s[start:end+1]
