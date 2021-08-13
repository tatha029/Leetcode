class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = set()
        def permuteHelper(already, remaining):
            if len(remaining) == 0:
                permutations.add(tuple(already))
            else:
                for i in range(len(remaining)):
                    permuteHelper(already+[remaining[i]], remaining[:i]+remaining[i+1:])
        permuteHelper([], nums)
        return [list(i) for i in permutations]
