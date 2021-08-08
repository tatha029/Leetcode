class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_path_sum = [0]*len(matrix)
        min_path_sum_dp = [0]*len(matrix)
        for i in reversed(range(len(matrix))):
            for j in range(len(matrix)):
                if j == 0 and j == len(matrix)-1:
                    min_path_sum[j] = matrix[i][j] + min_path_sum_dp[j]
                elif j == 0:
                    min_path_sum[j] = matrix[i][j] + min(min_path_sum_dp[j], min_path_sum_dp[j+1])
                elif j == len(matrix)-1:
                    min_path_sum[j] = matrix[i][j] + min(min_path_sum_dp[j-1], min_path_sum_dp[j])
                else:
                    min_path_sum[j] = matrix[i][j] + min(min_path_sum_dp[j-1], min_path_sum_dp[j], min_path_sum_dp[j+1])
            min_path_sum_dp = min_path_sum.copy()
        return min(min_path_sum)
