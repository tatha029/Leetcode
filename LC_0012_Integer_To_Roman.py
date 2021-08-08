class Solution:
    def intToRoman(self, num: int) -> str:
        thou = num//1000
        hund = (num%1000)//100
        ten = (num%100)//10
        one = num%10

        ans = ""
        ans += 'M'*thou
        if hund == 4:
            ans += 'CD'
        elif hund == 9:
            ans += 'CM'
        else:
            ans += 'D'*(hund//5) + 'C'*(hund%5)
        if ten == 4:
            ans += 'XL'
        elif ten == 9:
            ans += 'XC'
        else:
            ans += 'L'*(ten//5) + 'X'*(ten%5)
        if one == 4:
            ans += 'IV'
        elif one == 9:
            ans += 'IX'
        else:
            ans += 'V'*(one//5) + 'I'*(one%5)

        return ans
