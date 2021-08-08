class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchToPlace(nums, target):
            low, high = 0, len(nums)
            if target > nums[-1]:
                return high
            elif target < nums[0]:
                return low
            while low <= high:
                mid = (low+high)//2
                if nums[mid] < target and nums[mid+1] > target:
                    return mid+1
                if nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return -1

        if len(nums) == 0:
            return [-1,-1]
        lower, upper = searchToPlace(nums,target-0.5), searchToPlace(nums,target+0.5)
        if lower == upper:
            return [-1,-1]
        return [lower, upper-1]
