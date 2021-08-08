class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s):
            lptr, rptr = 0, len(s)-1
            while lptr < rptr:
                if s[lptr] != s[rptr]:
                    return False, lptr, rptr
                lptr += 1
                rptr -= 1
            return True, 0, 0

        isPal, lptr, rptr = checkPalindrome(s)
        if not isPal:
            left, right = checkPalindrome(s[:lptr]+s[lptr+1:]), checkPalindrome(s[:rptr]+s[rptr+1:])
            return left[0] or right[0]
        return isPal
