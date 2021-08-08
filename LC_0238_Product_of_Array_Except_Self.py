class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # calculate left products
        for i in range(len(nums)):
            if i == 0:
                res.append(1)
            else:
                res.append(res[i-1]*nums[i-1])
        # calculate right products
        for j in reversed(range(len(nums))):
            if j == len(nums)-1:
                R = 1
            else:
                R = R*nums[j+1]
            res[j] *= R
        return res
