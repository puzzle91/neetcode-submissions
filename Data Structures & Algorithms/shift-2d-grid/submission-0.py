class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

    

        rows = len(grid)
        cols = len(grid[0]) # can be 1 -- ok

        k = k % (rows * cols)

        for _ in range(k):

            prev = grid[-1][-1]

            for i in range(rows):
                for j in range(cols):
                    grid[i][j], prev = prev, grid[i][j]

        return grid
    


