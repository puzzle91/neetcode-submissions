import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distances = []

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(distances, (dist, p))

        res = []
        
        for _ in range(k):
            dist, point = heapq.heappop(distances)
            res.append(point)
        return res