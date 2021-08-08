class Solution:
    def numberToWords(self, num: int) -> str:
        #base case
        if num == 0:
            return 'Zero'

        # save num to array of 3 digit numbers
        splits = []
        while num > 0:
            splits.append(num%1000)
            num //= 1000
        # generate and store the int to eng of each number in array
        def smallNumToWords(sNum):
            digits = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',\
                      8:'Eight', 9:'Nine', 0:''}
            tensAlt = {1:'Eleven', 2:'Twelve', 3:'Thirteen', 4:'Fourteen', 5:'Fifteen', 6:'Sixteen',\
                       7:'Seventeen', 8:'Eighteen', 9:'Nineteen', 0:'Ten'}
            tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy',\
                    8:'Eighty', 9:'Ninety', 0:''}
            one = sNum%10
            ten = sNum//10 % 10
            hundr = sNum//100
            sNumStr = ''
            sNumStr += digits[hundr] + ' Hundred' if hundr > 0 else ''
            sNumStr += ' ' + tens[ten] if ten != 1 else ' ' + tensAlt[one]
            sNumStr += ' ' + digits[one] if ten != 1 else ''
            return ' '.join(sNumStr.split())
        # append billion, million as per necessary
        splitStr = [smallNumToWords(spl) for spl in splits]
        powers = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        ans = ''
        for i in reversed(range(len(splitStr))):
            if splitStr[i]:
                ans += ' ' + splitStr[i] + ' ' + powers[i]
        return ' '.join(ans.split())
