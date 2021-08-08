class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            idx = 0
            if needle == "":
                return 0
            idx = haystack.index(needle)
        except:
            idx = -1
        finally:
            return idx
