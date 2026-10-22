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
             
            tot = grid[i][j] + min(dfs(i + 1, j), dfs(i, j+1))
            cache[(i,j)] = tot
            return cache[(i,j)]
        ans = dfs(0,0)

        return ans