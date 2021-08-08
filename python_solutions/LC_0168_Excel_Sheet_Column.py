class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while columnNumber > 0:
            rem, quo = columnNumber % 26 - 1, columnNumber//26
            if rem == -1:
                quo -= 1
            res += alpha[rem]
            columnNumber = quo
        return res[::-1]
