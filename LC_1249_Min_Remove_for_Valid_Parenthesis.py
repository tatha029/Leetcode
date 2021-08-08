class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # keep in stack, pop when valid parenthesis found
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    # remove if no matching parens
                    s = s[:i] + '_' + s[i+1:]
        # remove all unmatched parens
        while stack:
            x = stack.pop()
            s = s[:x] + '_' + s[x+1:]

        s = s.replace('_', '')

        return s
