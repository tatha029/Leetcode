class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = [0]*60
        ans = 0
        for t in time:
            if rems[t%60] > 0:
                ans += rems[t%60]
            rems[(60 - t%60)%60] += 1
        return ans
