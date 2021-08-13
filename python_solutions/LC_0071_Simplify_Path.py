class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folders = path.split('/')
        for folder in folders:
            if folder == '' or folder == '.':
                continue
            elif folder == '..':
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(folder)
        return '/' + '/'.join(stack)
