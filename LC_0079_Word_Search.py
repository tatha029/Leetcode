class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, ind=0):
            if not board[i][j] or board[i][j] != word[ind]:
                return False
            if ind == len(word)-1 and board[i][j] == word[ind]:
                return True
            board[i][j] = False # keep track of visited cell
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                    if dfs(i+di, j+dj, ind+1):
                        return True
            board[i][j] = word[ind]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j):
                    return True
        return False
