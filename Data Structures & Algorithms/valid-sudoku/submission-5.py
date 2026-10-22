class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_size = len(board)
        col_size = len(board[0])
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        def dfs(i):
            if i == row_size * col_size: # all 81 spots are checked
                return True
            
            row, col = i//col_size, i % col_size 
            if board[row][col] == '.':
                return dfs(i + 1)
            
            square = (row // 3) * 3 + col // 3
            curr_value = board[row][col]
            # Already seen
            if curr_value in rows[row] or curr_value in cols[col] or curr_value in  squares[square]:
                return False
            else: 
                # otherwise continue exploring
                rows[row].add(curr_value)
                cols[col].add(curr_value)
                squares[square].add(curr_value)

            return dfs(i + 1)
        a = dfs(0)
        print(a)
        return a