from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # rowZero: whether the first row must be zeroed
        rowZero = False

        # 1) Use first row & first column as markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # 2) Zero cells based on markers (skip first row/col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:  # <-- fixed [0][c]
                    matrix[r][c] = 0

        # 3) First column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 4) First row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        