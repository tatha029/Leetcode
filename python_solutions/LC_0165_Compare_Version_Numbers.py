class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = [int(x) for x in version1.split('.')]
        ver2 = [int(x) for x in version2.split('.')]
        i = 0
        while i < min(len(ver1), len(ver2)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
            else:
                i += 1
        if (len(ver1) > len(ver2)) and sum(ver1[i:]) > 0:
            return 1
        if (len(ver1) < len(ver2)) and sum(ver2[i:]) > 0:
            return -1
        else:
            return 0
