class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        


        ROWS = len(grid)


        COLS = len(grid[0])

        fresh = 0


        visit = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

                if grid[r][c] == 1:
                    fresh += 1



        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        time = 0
        while fresh and q:

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if ((r + dr) not in range(ROWS) or (c + dc) not in range(COLS) or (r + dr, c + dc) in visit or grid[r + dr][c + dc] != 1):
                        continue

                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                    grid[r + dr][c + dc] = 2
                    fresh -= 1


            


            time += 1

        return time if fresh == 0 else -1