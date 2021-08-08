class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True] + [False]*len(s)

        for end in range(1, len(s)+1):
            for start in range(end):
                # if s[0:start] has valid decomposition and s[start:end] in wordDict
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True
        return dp[-1]
