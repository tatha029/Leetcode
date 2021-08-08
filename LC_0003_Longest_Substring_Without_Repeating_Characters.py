class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longSubstring, iterString, substringDict = "", "", {}
        for i in range(len(s)):
            if s[i] in substringDict.keys():
                if len(longSubstring) < len(iterString):
                    longSubstring = iterString
                # remove all from iterString and substringDict till s[i] is reached
                j = 0
                while iterString[j] != s[i]:
                    substringDict.pop(iterString[j])
                    j += 1
                iterString, substringDict[s[i]] = iterString[j+1:] + s[i], 1
            else:
                iterString += s[i]
                substringDict[s[i]] = 1
        if len(longSubstring) < len(iterString):
            longSubstring = iterString
        return len(longSubstring)
