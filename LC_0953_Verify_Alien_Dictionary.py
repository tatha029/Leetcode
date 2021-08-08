class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for idx, val in enumerate(order):
            orderMap[val] = idx

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # check for case 'apple' < 'app'
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if orderMap[words[i][j]] > orderMap[words[i+1][j]]:
                        return False
                    # if we find first distinct character that are sorted,
                    # then no need to check further
                    break
        return True
