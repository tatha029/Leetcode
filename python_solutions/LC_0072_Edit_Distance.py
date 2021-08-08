class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        # base cases
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
