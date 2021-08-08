class Solution:
    def modifyString(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        # handle edges
        if s == '?':
            return 'a'

        if s[0] == '?':
            for a in alpha:
                if a == s[1]:
                    continue
                else:
                    s = a + s[1:]

        if s[-1] == '?':
            for a in alpha:
                if a == s[-2]:
                    continue
                else:
                    s = s[:-1] + a

        # otherwise
        for i in range(1, max(1, len(s)-1)):
            if s[i] == '?':
                for a in alpha:
                    if a == s[i-1] or a == s[i+1]:
                        continue
                    else:
                        s = s[:i] + a + s[i+1:]
            else:
                continue

        return s
