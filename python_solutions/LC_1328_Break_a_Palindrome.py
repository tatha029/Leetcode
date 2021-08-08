class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # either substitute with a or b
        if len(palindrome) == 1:
            return ""
        i,j = 0, len(palindrome)-1
        while i < j:
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            i += 1
            j -= 1
        return palindrome[:-1] + 'b'
