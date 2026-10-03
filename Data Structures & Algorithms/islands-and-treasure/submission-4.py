class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid or not grid[0]:
            return
        visit = set()


        q = deque()


        ROWS, COLS = len(grid), len(grid[0])


        def helper(r, c):

            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c] == -1 or (r, c) in visit):
                return

            visit.add((r, c))

            q.append((r, c))





        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

                    visit.add((r, c))


        
        dist = 0
        while q:
            

            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist


                helper(r + 1, c)

                helper(r - 1, c)

                helper(r, c + 1)

                helper(r, c - 1)

            dist += 1

    


        
            





