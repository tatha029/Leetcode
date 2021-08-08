class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # only positive number will pass
        rev, x_copy = 0, x
        while x > 0:
            rev = rev*10 + x%10
            x //= 10
        return rev == x_copy
