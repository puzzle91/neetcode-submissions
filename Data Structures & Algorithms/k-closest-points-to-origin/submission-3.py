import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        origin = (0,0)
        
        distances = []
        for p in points:
            dist = (p[0]**2 + p[1]**2) 
            heapq.heappush(distances, (dist, p))
        
        res = []
        for _ in range(k):
            v = heapq.heappop(distances)
            res.append(v[1])
        return res