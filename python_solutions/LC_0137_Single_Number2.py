class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        x = sum(list(set(nums)))
        return (3*x - s)//2
