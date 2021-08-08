class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # enforce a as the largest string
        l1, l2 = len(a), len(b)
        if l1 < l2:
            l1, l2, a, b = l2, l1, b, a
        carry = 0
        res = ""
        for i in range(-1, -l2-1, -1):
            x, y = int(a[i]), int(b[i])
            res += str(x ^ y ^ carry)
            carry = (x and y) or (y and carry) or (x and carry)
        for i in range(-l2-1, -l1-1, -1):
            x = int(a[i])
            res += str(x ^ carry)
            carry = x and carry
        if carry:
            res += str(carry)

        return res[::-1]
