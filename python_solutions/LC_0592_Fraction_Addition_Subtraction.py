class Solution:
    def fractionAddition(self, expression: str) -> str:
        def addToResult(resNum, resDen, inter):
            if inter != '':
                x = inter.index('/')
                aNum, aDen = int(inter[:x]), int(inter[x+1:])
                resNum, resDen = aNum*resDen + aDen*resNum, aDen*resDen
                div = gcd(resNum, resDen)
                resNum, resDen = int(resNum/div), int(resDen/div)
            return resNum, resDen

        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a

        resNum, resDen = 0, 1
        inter = ''
        for i in range(len(expression)):
            if expression[i] in '+-':
                resNum, resDen = addToResult(resNum, resDen, inter)
                inter = expression[i] # start with + or -
            else:
                inter += expression[i]
        resNum, resDen = addToResult(resNum, resDen, inter)
        return f'{resNum}/{resDen}'
