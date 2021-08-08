class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search location where x can lie in arr
        # insert into a heap k elements on right and k elements on left
        heap = [(abs(x - arr[i]), arr[i]) for i in range(len(arr))]
        lst = [i for _,i in heapq.nsmallest(k, heap)]
        lst.sort()
        return lst
