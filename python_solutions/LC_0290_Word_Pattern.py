class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strMap = {}
        patMap = {}
        sList = s.split(' ')
        if len(sList) != len(pattern):
            return False
        for i in range(len(pattern)):
            if (pattern[i] not in strMap) and (sList[i] not in patMap):
                strMap[pattern[i]] = sList[i]
                patMap[sList[i]] = pattern[i]
            elif (sList[i] in patMap) and (patMap[sList[i]] != pattern[i]):
                return False
            elif (pattern[i] in strMap) and (strMap[pattern[i]] != sList[i]):
                return False
        return True
