# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            # nothing to check
            return 1

        low, high = 1, n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                # if true, then bad version is before or at mid
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1
            else:
                # if false, bad version is after mid
                low = mid + 1
