class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(x,y) for (x,y) in zip(position,speed)]
        cars.sort(reverse=True)
        dist = [False] * len(cars)
        fleets = 0
        curr_max_time = 0
        #print(cars)
        for idx, (p,s) in enumerate(cars):
            time = (target- p) / s
            dist[idx] = time
            if time > curr_max_time:
                curr_max_time = time
                fleets +=1 
        #print(dist, fleets, curr_max_time)
        return fleets