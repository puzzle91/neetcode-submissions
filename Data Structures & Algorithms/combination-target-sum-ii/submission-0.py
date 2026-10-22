class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        mem_cache ={}
        def backtrack(idx, path, tot):
            if tot == 0:
                res.append(path[:])
                return 
            
            
            mem_cache[tot] = path

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if tot - candidates[i] < 0:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, tot - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return res