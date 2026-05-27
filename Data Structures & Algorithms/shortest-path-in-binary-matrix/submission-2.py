class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        N = len(grid)

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque([(0, 0 , 1)])
        if grid[0][0] == 1:
            return -1
        visit = set((0, 0))
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:

            r, c, length = q.popleft()
            

            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:

                row, col = r + dr, c + dc


                if (min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visit or grid[row][col] == 1):
                    continue


                q.append([row, col, length + 1])

                visit.add((row, col))


        return -1

            