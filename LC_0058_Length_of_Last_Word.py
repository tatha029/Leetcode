class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, lenWord = len(s)-1, 0
        # search for first word
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            i -= 1
            lenWord += 1
        return lenWord
