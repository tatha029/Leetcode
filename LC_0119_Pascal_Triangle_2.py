class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            if i == 0:
                pascal_triangle = [1]
                continue
            pascal_triangle = [i+j for i, j in zip(pascal_triangle+[0], [0]+pascal_triangle)]
        return pascal_triangle
