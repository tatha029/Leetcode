class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num2 should be smaller of the two
        len1, len2 = len(num1), len(num2)
        if len1 < len2:
            num1, num2, len1, len2 = num2, num1, len2, len1
        # prepend num2 with 0s
        num2 = '0'*(len1-len2) + num2

        carry, ans = 0, ""
        for i in reversed(range(len1)):
            ans += str((int(num1[i]) + int(num2[i]) + carry)%10)
            carry = (int(num1[i]) + int(num2[i]) + carry)//10

        if carry > 0:
            ans += str(carry)

        return ans[::-1]
