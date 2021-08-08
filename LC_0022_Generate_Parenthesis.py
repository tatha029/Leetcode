import itertools
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenListGlobal = {0:[""], 1:["()"]}
        def generateParenthesisHelper(n):
            if n in parenListGlobal.keys():
                return parenListGlobal[n]
            parensList = []
            for x in generateParenthesisHelper(n-1):
                parensList += ['()'+x, '('+x+')', x+'()']
            for i in range(1,n):
                parensList += [x+y for x,y in itertools.product(generateParenthesisHelper(i),\
                                                                generateParenthesisHelper(n-i))]
            parenListGlobal[n] = parensList
            return list(set(parensList))
        return generateParenthesisHelper(n)
