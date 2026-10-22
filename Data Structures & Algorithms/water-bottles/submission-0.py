class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tot = 0
        tot = numBottles 
        exchanges = 0
        empty =tot

        while empty >= numExchange:
            full = empty // numExchange
            rmainder = empty % numExchange

            tot += full
            empty = full + rmainder
        return tot
        