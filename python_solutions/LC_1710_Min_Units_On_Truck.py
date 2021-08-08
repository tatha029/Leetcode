class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:-x[1])
        i = 0
        tot = 0
        while truckSize > 0 and i < len(boxTypes):
            if truckSize > boxTypes[i][0]:
                tot += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                tot += truckSize * boxTypes[i][1]
                truckSize = 0
            i += 1
        return tot
