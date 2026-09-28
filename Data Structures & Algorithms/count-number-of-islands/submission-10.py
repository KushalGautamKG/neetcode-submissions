class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        if not grid:
            return 0


        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        q = deque()
        def bfs(r, c):

            q.append((r, c))

            visit.add((r, c))


            while q:

                row, col = q.popleft()


                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:


                    r, c = row + dr, col + dc

                    if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or grid[r][c] != "1"):
                        continue


                    visit.add((r, c))
                    q.append((r, c))








        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:

                    bfs(r, c)
                    islands += 1
        return islands
