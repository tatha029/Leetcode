class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path_sum = [0]*(len(triangle)+1)
        for i in reversed(range(len(triangle))):
            for j in range(i+1):
                min_path_sum[j] = triangle[i][j] + min(min_path_sum[j], min_path_sum[j+1])
        return min_path_sum[0]
