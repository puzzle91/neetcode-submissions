import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cache = defaultdict(int)

        for n in nums:
            cache[n] +=1
        res = [x[0] for x in sorted(cache.items(), key = lambda x: x[1], reverse=True)[:k]]
        return res