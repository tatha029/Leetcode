class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for indStr in strs:
            x = ''.join(sorted(indStr))
            if x in hashMap:
                hashMap[x].append(indStr)
            else:
                hashMap[x] = [indStr]
        res = []
        for key, lst in hashMap.items():
            res.append(lst)
        return res
