class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ist = sorted(zip(indexes, sources, targets), key=lambda x: x[0])
        res = []
        st = 0

        for i, s, t in ist:
            res.append(S[st:i])
            if S[i:i+len(s)] == s:
                res.append(t)
            else:
                res.append(S[i:i+len(s)])
            st = i + len(s)
        return ''.join(res) + S[st:]
