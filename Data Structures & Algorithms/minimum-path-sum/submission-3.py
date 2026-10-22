class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        grid_row = len(grid)
        grid_col = len(grid[0])
        path = []
        cache = {}
        def dfs(i,j):
            if i >= grid_row or j >= grid_col:
                return float('inf')
            if i  == grid_row - 1 and j== grid_col-1:
                return grid[i][j]
            
            mvs = [(0,1), (1,0)]
            if (i,j) in cache:
                return cache[(i,j)]
             
            lowest_val = float("inf")
            mvs = [(0, 1), (1, 0)]

            for di, dj in mvs:
                new_i, new_j = i + di, j + dj
                cost = grid[i][j] + dfs(new_i, new_j)
                lowest_val = min(lowest_val, cost)
            cache[(i,j)] = lowest_val
            return cache[(i,j)]
        ans = dfs(0,0)

        return ans