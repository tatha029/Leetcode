class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def permuteHelper(already, remaining):
            if len(remaining) == 0:
                permutations.append(already)
            else:
                for i in range(len(remaining)):
                    permuteHelper(already+[remaining[i]], remaining[:i]+remaining[i+1:])
        permuteHelper([], nums)
        return permutations
