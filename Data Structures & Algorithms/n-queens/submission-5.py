class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        cols = set()
        postDiag = set()

        negDiag = set()

        board = [["."] * n for _ in range(n)]

        res = []

        def dfs(r):

            if r == n:
                copy = ["".join(n) for n in board]

                res.append(copy)


                return


            

            
            for c in range(n):
                
                if (r + c) in postDiag or (r - c) in negDiag or c in cols:
                    continue
                cols.add(c)

                postDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"

                dfs(r + 1)

                board[r][c] = "."

                cols.remove(c)
                postDiag.remove(r + c)

                negDiag.remove(r - c)

        dfs(0)

        return res