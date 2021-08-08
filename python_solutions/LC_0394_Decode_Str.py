class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        stack=[]
        res=''
        for i in range (len(s)):
            sn=''
            if not stack and s[i].isalpha():
                res+=s[i]
            else:
                if s[i]!=']':
                    stack.append(s[i])
                else:
                    while (stack and stack[-1]!='['):
                        t=stack.pop()
                        sn+=t
                    stack.pop()
                    rt=''
                    while (stack and stack[-1].isdigit()):
                        rt+=stack.pop()
                    no=int(rt[::-1])
                    if stack and '[' in stack:
                        rev=no*(sn)
                        stack.append(rev)
                    else:
                        rev=no*(sn[::-1])
                        res+=rev
        return res
