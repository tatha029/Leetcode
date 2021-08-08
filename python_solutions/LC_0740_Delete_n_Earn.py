from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        prev = None
        avoid, using = 0, 0
        for k in sorted(freq):
            if k-1 != prev:
                avoid, using = max(avoid, using), k*freq[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*freq[k] + avoid
            prev = k
        return max(avoid, using)
