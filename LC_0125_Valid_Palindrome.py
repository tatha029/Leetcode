class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        head, tail = 0, len(s)-1
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True
