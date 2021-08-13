class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # first row are of form k(2*numRows-2)
        # ith row is of form k(2*num-2)(-i and +i)
        # last row is of the form (numRows-1) + k(numRows-1)
        if numRows == 1:
            return s

        n, cycle = len(s), 2*numRows-2
        newStr = ""
        for i in range(numRows):
            for j in range(0,n-i,cycle):
                newStr += s[j+i]
                if i != 0 and i != numRows-1 and j+cycle-i < n:
                    newStr += s[j+cycle-i]

        return newStr
