class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evalExpr(a, b, operand):
            if operand == '+':
                return str(int(a) + int(b))
            if operand == '-':
                return str(int(a) - int(b))
            if operand == '*':
                return str(int(a) * int(b))
            return str(int(int(a) / int(b)))

        stack = []
        for token in tokens:
            if token in '+-*/':
                b, a = stack.pop(), stack.pop()
                stack.append(evalExpr(a, b, token))
            else:
                stack.append(token)
        return int(stack.pop())
