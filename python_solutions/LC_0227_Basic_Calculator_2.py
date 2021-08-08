class Solution:
    def calculate(self, s: str) -> int:
        # extract to list
        numStack = []
        num = ''
        for i in s:
            if i == ' ':
                continue
            if i not in '+-/*':
                num += i
            else:
                numStack.append(int(num))
                numStack.append(i)
                num = ''
        numStack.append(int(num))
        # calculate multiplication and division
        i = 0
        while i < len(numStack):
            if numStack[i] == '*':
                numStack[i-1] = numStack[i-1]*numStack[i+1]
                del numStack[i:i+2]
                continue
            elif numStack[i] == '/':
                numStack[i-1] = numStack[i-1]//numStack[i+1]
                del numStack[i:i+2]
                continue
            i += 1
        # calculate addition and subtraction
        i = 0
        while i < len(numStack):
            if numStack[i] == '+':
                numStack[i-1] = numStack[i-1]+numStack[i+1]
                del numStack[i:i+2]
                continue
            elif numStack[i] == '-':
                numStack[i-1] = numStack[i-1]-numStack[i+1]
                del numStack[i:i+2]
                continue
            i += 1
        return numStack[0]
