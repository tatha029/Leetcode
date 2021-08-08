from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec = Counter(secret)
        gue = Counter(guess)
        bulls, cows = 0, 0
        for k in gue:
            if k in sec:
                cows += min(sec[k], gue[k])

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                cows -= 1
                bulls += 1

        return f"{bulls}A{cows}B"
