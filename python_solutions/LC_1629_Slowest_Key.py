class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxm, idx = releaseTimes[0], 0
        for i in range(1, len(keysPressed)):
            d = releaseTimes[i] - releaseTimes[i-1]
            if d > maxm:
                maxm, idx = d, i
            elif d == maxm:
                if keysPressed[idx] < keysPressed[i]:
                    idx = i
        return keysPressed[idx]
