from functools import cache
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        @cache
        def create_row(n):
            if n == 0:
                return (1,)
            prev = create_row(n - 1)
            
            new_row =  (1,) + tuple(prev[i] + prev[i + 1] for i in range(n - 1)) + (1,)
            #print('prev', prev, 'newrow',new_row)
            return new_row
        
        return [list(create_row(n)) for n in range(numRows)]