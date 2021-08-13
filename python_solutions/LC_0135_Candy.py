class Solution:
    def candy(self, ratings: List[int]) -> int:
        left, right = [1], [1]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left.append(left[-1]+1)
            else:
                left.append(1)

        for i in reversed(range(len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                right.append(right[-1]+1)
            else:
                right.append(1)

        res = [max(l, r) for l, r in zip(left, reversed(right))]
        return sum(res)
