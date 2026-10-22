class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        mvs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def dfs(idx, start):
            if start == len(word):
                return True
            i,j = idx
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            if idx in visited:
                return False
                
            if board[i][j] == word[start]:
                visited.add(idx)
            else:
                return False
                
            
            for mv in mvs:
                    if dfs((i+mv[0], j+mv[1]), start +1):
                        return True
             # Backtrack
            visited.remove(idx)
            return False
            
       
        # Try every cell as a starting position
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs((i, j), 0):
                    return True

        return False