class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        rs = [0]
        for i in range(len(nums)):
            rs.append(rs[-1]+nums[i])
        self._rangeSums = rs

    def sumRange(self, left: int, right: int) -> int:
        return self._rangeSums[right+1] - self._rangeSums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
