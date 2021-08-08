class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = False
        if (numerator * denominator < 0):
            neg = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        quo = numerator // denominator
        rem = numerator % denominator
        res = [('-' if neg else '') + str(quo)]
        visited = {}
        if rem == 0:
            return res[0]
        else:
            res.append('.')
            while rem > 0:
                if rem in visited:
                    res.append(')')
                    res.insert(visited[rem], '(')
                    break
                else:
                    visited[rem] = len(res)
                    rem *= 10
                    res.append(str(rem//denominator))
                    rem %= denominator
        return ''.join(res)
