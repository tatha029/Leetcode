class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for i in range(numRows):
            if i == 0:
                pascal_triangle.append([1])
                continue
            c = [i+j for i, j in zip(pascal_triangle[-1]+[0], [0]+pascal_triangle[-1])]
            pascal_triangle.append(c)
        return pascal_triangle
