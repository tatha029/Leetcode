class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        s_hash = {}
        for i in range(len(s)):
            if s[i] not in s_hash:
                s_hash[s[i]] = i
            else:
                s_hash[s[i]] = len(s)+1
        idx = min(s_hash.values())
        if idx == len(s)+1:
            idx = -1
        return idx
