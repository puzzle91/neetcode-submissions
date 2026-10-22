class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        fresh = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1 

        #up, down, left, right
        mvs = [(-1, 0), (1, 0), (0,-1), (0,1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                i,j = q.popleft()

                #new moves
                for dx,dy in mvs:
                    ni,nj = i+dx,j+dy
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        q.append((ni, nj))
                        grid[ni][nj] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1