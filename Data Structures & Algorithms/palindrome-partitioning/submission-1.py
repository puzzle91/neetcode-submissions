class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        seen = {}
        def backtrack(start, path):
          
            
            
            if start == len(s):
               
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
                   
            
        backtrack(0, [])
        #print(res)
        return res