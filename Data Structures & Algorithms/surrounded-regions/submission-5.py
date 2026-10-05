class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        ROWS, COLS = len(board), len(board[0])
        visit = set()
        
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O" or (r, c) in visit:
                return

            board[r][c] = "T"
            dfs(r + 1, c)

            dfs(r - 1, c)

            dfs(r, c + 1)
            dfs(r, c - 1)


        


        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1):
                    dfs(r, c)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"