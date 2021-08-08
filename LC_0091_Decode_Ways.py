class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def numDecodeHelper(s):
            if not s:
                return 1
            valid = 0
            if 1 <= int(s[:1]) <= 26:
                valid = numDecodeHelper(s[1:])
                if len(s) > 1 and 1 <= int(s[:2]) <= 26:
                    valid += numDecodeHelper(s[2:])
            return valid
        return numDecodeHelper(s)
