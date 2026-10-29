class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        N = len(grid)

        


        minH = [(grid[0][0], 0, 0)]

        res = 0
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minH:

            t, r, c = heapq.heappop(minH)
            

            if r == N - 1 and c == N - 1:
                return t
            if (r, c) in visit:
                continue

            visit.add((r, c))




            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (row not in range(N) or col not in range(N) or (row, col) in visit):
                    continue


                heapq.heappush(minH, (max(t, grid[row][col]), row, col))



        

                

            

