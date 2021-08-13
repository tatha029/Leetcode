class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        num, l = 1, 0
        while True:
            # right
            for j in range(l, n-l):
                i = l
                matrix[i][j] = num
                num += 1
            if num == n*n + 1:
                break
            # down
            for i in range(l+1, n-l):
                j = n-l-1
                matrix[i][j] = num
                num += 1
            if num == n*n + 1:
                break
            # left
            for j in reversed(range(l, n-l-1)):
                i = n-l-1
                matrix[i][j] = num
                num += 1
            if num == n*n + 1:
                break
            # up
            for i in reversed(range(l+1, n-l-1)):
                j = l
                matrix[i][j] = num
                num += 1
            if num == n*n + 1:
                break
            l += 1
        return matrix
