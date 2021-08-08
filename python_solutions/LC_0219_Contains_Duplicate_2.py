class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window, windowSize = set(), 0
        if k == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            else:
                if windowSize == k:
                    window.remove(nums[i-k])
                    windowSize -= 1
                window.add(nums[i])
                windowSize += 1
        return False
