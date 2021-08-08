class Solution:
    def compress(self, chars: List[str]) -> int:
        curr, ctr, charIter = chars[0], 0, 0
        for i in range(len(chars)):
            if chars[i] == curr:
                ctr += 1
            else:
                chars[charIter] = curr
                charIter += 1
                if ctr > 1:
                    for j in range(len(str(ctr))):
                        chars[charIter] = str(ctr)[j]
                        charIter += 1
                curr, ctr = chars[i], 1
        chars[charIter] = curr
        charIter += 1
        if ctr > 1:
            for j in range(len(str(ctr))):
                chars[charIter] = str(ctr)[j]
                charIter += 1
        return charIter
