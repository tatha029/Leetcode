class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, i = 1, len(digits)-1
        while carry > 0 and i >= 0:
            digits[i], carry = (digits[i] + carry)%10, (digits[i] + carry)//10
            i -= 1
        if carry == 1:
            return [1] + digits
        else:
            return digits
