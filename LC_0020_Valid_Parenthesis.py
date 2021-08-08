class Solution:
    def isValid(self, s: str) -> bool:
        opens, closes = '({[', ')}]'
        open_stack = []
        for i in range(len(s)):
            if s[i] in opens:
                open_stack.append(s[i])
            else: # it is closed
                if len(open_stack) == 0:
                    return False
                elif s[i] == closes[opens.index(open_stack[-1])]:
                    x = open_stack.pop()
                else:
                    return False
        return len(open_stack) == 0
