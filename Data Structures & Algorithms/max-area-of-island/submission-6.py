class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()


        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or grid[r][c] != 1):
                return 0

            visit.add((r, c))

            res = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


            return res
        






        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):

                maxArea = max(maxArea, dfs(r, c))


        return maxArea
