class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = [0] + arr
        diff = [arr[i]-i for i in range(len(arr))]
        # below can be done using binary search and not using diff arr
        # but that is not an easy task
        for i in range(1, len(diff)):
            if diff[i] >= k:
                return arr[i-1] + k - diff[i-1]
        return arr[-1] + k - diff[-1]
