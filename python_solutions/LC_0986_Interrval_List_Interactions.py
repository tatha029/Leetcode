class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len1, len2 = len(firstList), len(secondList)
        if len1 == 0 or len2 == 0:
            return []
        i = j = 0
        res = []
        while i < len1 and j < len2:
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                res.append([lo, hi])

            # remove interval with smallest endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res
