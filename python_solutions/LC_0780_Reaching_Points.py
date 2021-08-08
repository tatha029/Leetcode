class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        return (sx == tx and ty >= sy and (ty - sy) % sx == 0) \
                or (sy == ty and tx >= sx and (tx - sx) % sy == 0)
