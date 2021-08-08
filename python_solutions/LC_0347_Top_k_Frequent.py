from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(value, key) for key, value in Counter(nums).items()]
        largest = heapq.nlargest(k, heap)
        largest = [key for _, key in largest]
        return largest
