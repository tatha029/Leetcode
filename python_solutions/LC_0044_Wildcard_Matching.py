class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)

        # base cases
        if p == s or set(p) == set('*'):
            return True
        if p == '' or s == '':
            return False

        dp = [[False for _ in range(pLen+1)] for _ in range(sLen+1)]
        dp[0][0] = True

        j = 0
        while j < pLen and p[j] == '*':
            for i in range(sLen+1):
                dp[i][j+1] = True
            j += 1

        for i in range(1, sLen+1):
            for j in range(1, pLen+1):
                if p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
