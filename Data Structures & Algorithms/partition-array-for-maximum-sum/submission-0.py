class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        res = []
        cache = {}
        def backtrack(start):
            if start == len(arr):
                return 0
            if start in cache:
                return cache[start]
            best, group_max = 0,0
            for i in range(start, min(start + k, len(arr))):
                group_max = max(group_max, arr[i])
                size = i - start + 1
                total = group_max * size + backtrack(i+1)
                best = max(best, total)
            cache[start] = best
            return best
        return backtrack(0)

 