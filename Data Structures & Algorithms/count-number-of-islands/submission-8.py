class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        if not grid:
            return 0


        ROWS = len(grid)
        islands = 0

        COLS = len(grid[0])
        visit = set()

        def bfs(r, c):

            q = deque()

            

            visit.add((r, c))

            q.append((r, c))

            while q:
                r, c = q.popleft()

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:

                    row, col = r + dr, c + dc

                    if (row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visit or grid[row][col] != '1'):
                        continue

                    q.append((row, col))
                    visit.add((row, col))


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    bfs(r, c)

                    islands += 1

        return islands
