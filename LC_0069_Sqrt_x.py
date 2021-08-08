class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0 or x > 2**31:
            return
        low, high, mid = 0, x, 0
        while low <= high:
            mid = (low+high)//2
            if mid**2 <= x and (mid+1)**2 > x:
                break
            elif mid**2 > x:
                high = mid
            else:
                low = mid+1
        return mid
