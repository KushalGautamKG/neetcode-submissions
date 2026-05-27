from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0


        ROWS, COLS = len(grid), len(grid[0])


        visit = set()


        islands = 0



        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def bfs(r, c):

            q = collections.deque()
            visit.add((r, c))


            q.append((r, c))


            while q:

                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != "1" or (row, col) in visit):
                        continue


                    q.append((row, col))

                    visit.add((row, col))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands




