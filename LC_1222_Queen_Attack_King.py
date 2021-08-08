class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        killerQueens = {} # queens that kills

        def queenKillsKing(queen):
            r, c = queen[0] - king[0], queen[1] - king[1]
            norm = max(abs(r), abs(c))
            direction = (r//norm, c//norm)
            if r == 0 or c == 0 or abs(r) == abs(c):
                return True, direction
            return False, (0,0)

        def canCurrentKill(queen, direction):
            if str(direction) not in killerQueens:
                killerQueens[str(direction)] = queen
            else:
                insertedQueen = killerQueens[str(direction)]
                rangeX = (min(insertedQueen[0]*direction[0], king[0]*direction[0]),
                          max(insertedQueen[0]*direction[0], king[0]*direction[0])+1)
                rangeY = (min(insertedQueen[1]*direction[1], king[1]*direction[1]),
                          max(insertedQueen[1]*direction[1], king[1]*direction[1])+1)
                dirX, dirY = queen[0]*direction[0], queen[1]*direction[1]
                if dirX in range(rangeX[0], rangeX[1]) and dirY in range(rangeY[0], rangeY[1]):
                    killerQueens[str(direction)] = queen

        for queen in queens:
            kills, direction = queenKillsKing(queen)
            if kills:
                canCurrentKill(queen, direction)
            else:
                continue
        res = []
        for _, val in killerQueens.items():
            res.append(val)
        return res
