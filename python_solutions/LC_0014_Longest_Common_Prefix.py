class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        def longestCommonPrefixHelper(s1, s2):
            idx, min_len = 0, min(len(s1), len(s2))
            while idx < min_len and s1[idx] == s2[idx]:
                idx += 1
            return s1[:idx]
        pref = strs[0]
        for i in range(1, len(strs)):
            pref = longestCommonPrefixHelper(pref, strs[i])
            if pref == "":
                break
        return pref
