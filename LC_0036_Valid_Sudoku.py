class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows:
        for i in range(9):
            checkSet = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in checkSet:
                        checkSet.add(board[i][j])
                    else:
                        return False
        # check cols:
        for i in range(9):
            checkSet = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in checkSet:
                        checkSet.add(board[j][i])
                    else:
                        return False
        # check squares:
        for k in range(3):
            for l in range(3):
                checkSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[3*l+i][3*k+j] != ".":
                            if board[3*l+i][3*k+j] not in checkSet:
                                checkSet.add(board[3*l+i][3*k+j])
                            else:
                                return False
        return True
