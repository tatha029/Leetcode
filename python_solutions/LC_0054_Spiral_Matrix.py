class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, l = len(matrix), len(matrix[0]), 0
        res, resLen = [], 0
        while True:
            # right
            for j in range(l, n-l):
                i = l
                res.append(matrix[i][j])
                resLen += 1
            if resLen == m*n:
                break
            # down
            for i in range(l+1, m-l):
                j = n-l-1
                res.append(matrix[i][j])
                resLen += 1
            if resLen == m*n:
                break
            # left
            for j in reversed(range(l, n-l-1)):
                i = m-l-1
                res.append(matrix[i][j])
                resLen += 1
            if resLen == m*n:
                break
            # up
            for i in reversed(range(l+1, m-l-1)):
                j = l
                res.append(matrix[i][j])
                resLen += 1
            if resLen == m*n:
                break
            l += 1
        return res
