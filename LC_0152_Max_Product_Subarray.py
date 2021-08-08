class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = _max = nums[0]
        for n in nums[1:]:
            cur_max, cur_min = max(cur_max*n, cur_min*n, n), min(cur_max*n, cur_min*n, n)
            _max = max(cur_max, _max)
        return _max
