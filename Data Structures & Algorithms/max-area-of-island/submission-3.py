class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(loc, seen = None):
            i,j = loc

            if i < 0 or j < 0 or i >= len(grid) or j>= len(grid[0]):
                return 0
            
            if grid[i][j] == 0 or loc in seen:
                return 0
            
            area = 1
            seen.add(loc)

            #up,down,left,right:
            moves = [(-1,0), (1,0), (0,-1), (0,1)]

            for dx, dy in moves:
                new_i, new_j = i + dx, j+dy
                 
                loc = (new_i, new_j)
                area += dfs(loc=loc, seen = seen)
            
            return area 


        max_area = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] == 1:
                    area = dfs((i,j), seen)
                   
                    max_area = max(area, max_area)
        return max_area


