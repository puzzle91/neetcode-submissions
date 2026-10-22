class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for j in range(9):
            seen_col = set()
            seen_row = set()
            for k in range(9):
                row_ = board[j][k]
                col_ = board[k][j]
         
                if  col_ != '.':
                    if col_ not in seen_col:
                        seen_col.add(col_)
                    else:
                        return False
                if  row_ != '.':
                    if row_ not in seen_row:
                        seen_row.add(row_)
                    else:
                        return False
              
        
        for cube in range(9):
            
            cube_seen =  set()
            row_start = (cube // 3) * 3
            col_start = (cube % 3) * 3
            for z in range(3):
                for i in range(3):
                    cube_val = board[row_start + z][col_start + i]
                    print(cube_val, 'cube_val')
                    if cube_val != '.':
                        if cube_val not in cube_seen:
                            cube_seen.add(cube_val)
                        else:
                            print("HERE", cube_val)
                            return False
        return True
                