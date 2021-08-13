from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # clean up nums : since a number can only feature 4 times,
        # remove all instances of number > 4 times
        numCtr = Counter(nums)
        numsClr = []
        for i in numCtr:
            numsClr += [i]*(min(numCtr[i], 4))
        nums = numsClr

        twoSum = {}
        x = len(nums)
        for i in range(x-1):
            for j in range(i+1, x):
                s = nums[i] + nums[j]
                if s in twoSum:
                    twoSum[s].append((i,j))
                else:
                    twoSum[s] = [(i,j)]

        res = set()
        for i in range(x-1):
            for j in range(i+1, x):
                s = target - nums[i] - nums[j]
                if s in twoSum:
                    for ts in twoSum[s]:
                        if i != ts[0] and i != ts[1] and \
                           j != ts[0] and j != ts[1] :
                            arr = [nums[ts[0]], nums[ts[1]], \
                                   nums[i], nums[j]]
                            arr.sort()
                            if tuple(arr) not in res:
                                res.add(tuple(arr))

        res = [list(i) for i in res]
        return res
