class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letLogs, digLogs = [], []
        for log in logs:
            x = log.split()
            if x[1][0] in '0123456789':
                # it is a digit-log
                digLogs.append((x[0], ' '.join(x[1:])))
            else:
                # it is a letter-log
                letLogs.append((x[0], ' '.join(x[1:])))
        letLogs = sorted(letLogs, key=lambda x: (x[1], x[0]))
        return [i + ' ' + j for i,j in letLogs] + [i + ' ' + j for i,j in digLogs]
