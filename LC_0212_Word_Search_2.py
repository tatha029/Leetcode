class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # either caching some sequences or initial removal of words can be done
        # one edge case had letters in search word that were not in board
        def exists(word):
            @cache
            def dfs(i, j, ind=0):
                if not board[i][j] or board[i][j] != word[ind]:
                    return False
                if ind == len(word)-1 and board[i][j] == word[ind]:
                    return True
                board[i][j] = False # keep track of visited cell
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]):
                        if dfs(i+di, j+dj, ind+1):
                            board[i][j] = word[ind]
                            return True
                board[i][j] = word[ind]

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if dfs(i, j):
                        return True
            return False

        res = []
        for word in words:
            if exists(word):
                res.append(word)
        return res
