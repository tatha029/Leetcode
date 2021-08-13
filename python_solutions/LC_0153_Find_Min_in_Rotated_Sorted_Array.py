class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
        if low == high:
            return nums[low]
