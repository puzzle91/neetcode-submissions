class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #find the row
        num_rows = len(matrix) 
        num_cols = len(matrix[0])


        for row in range(num_rows):
            start = matrix[row][0] 
            end  = matrix[row][-1]
            if start <= end:

                if target in range(start-1, end + 1):
                    print(f"target {target} in range({start}, {end})")
                    for val in range(num_cols):
                        print(matrix[row][val], "checking here")
                        if target == matrix[row][val]:
                            return True
        return False
                
            
                
                