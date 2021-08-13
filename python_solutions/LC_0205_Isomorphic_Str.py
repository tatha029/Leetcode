class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def checkMutability(s, t):
            hashMap = {}
            for i in range(len(s)):
                if s[i] not in hashMap:
                    hashMap[s[i]] = t[i]
                elif hashMap[s[i]] != t[i]:
                        return False
                else:
                    continue
            return True
        return checkMutability(s, t) and checkMutability(t, s)
