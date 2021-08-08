class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def getOrigZeroes(matrix):
            rows, cols = [], []
            for i in range(num_rows):
                for j in range(num_cols):
                    if matrix[i][j] == 0:
                        rows.append(i)
                        cols.append(j)
            rows, cols = list(set(rows)), list(set(cols))
            return rows, cols

        if not matrix:
            return
        num_rows, num_cols = len(matrix), len(matrix[0])
        rows, cols = getOrigZeroes(matrix)
        for row in rows:
            matrix[row] = [0]*num_cols
        for i in range(num_rows):
            for col in cols:
                matrix[i][col] = 0
