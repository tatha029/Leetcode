class Solution:
    def reverseWords(self, s: str) -> str:
        # python doesn't allow in space mutation of string so O(1) solution is not possible
        return " ".join(reversed(s.split()))
