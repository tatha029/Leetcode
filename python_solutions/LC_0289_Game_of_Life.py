class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_nbr = 0
                for nbr in neighbours:
                    r, c = row + nbr[0], col + nbr[1]
                    # check validity of nbr cells as well
                    if (r<rows and r>=0) and (c<cols and c>=0) and abs(board[r][c]) == 1:
                        live_nbr += 1
                # Under and Over Population Rules
                if (board[row][col] == 1) and (live_nbr < 2 or live_nbr > 3):
                    board[row][col] = -1
                # Reproduction
                if (board[row][col] == 0) and (live_nbr == 3):
                    board[row][col] = 2

        # Final cleaning of updated board
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
