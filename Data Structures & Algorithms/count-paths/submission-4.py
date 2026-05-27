class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n


        for i in range(m - 1):

            newRow = [0] * n

            newRow[n - 1] = 1

            for j in range(n - 2, -1, -1):

                newRow[j] = row[j] + newRow[j + 1]


            row = newRow

        return row[0]

            
