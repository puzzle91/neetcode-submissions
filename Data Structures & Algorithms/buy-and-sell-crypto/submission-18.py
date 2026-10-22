class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = min(prices)
         


        best_price = prices[0]
        sell_price = prices[-1]

        profit =  best_price - sell_price 
        max_profit = 0
        for i in range(len(prices)):
            
            if prices[i] <= best_price:
                best_price = prices[i]
                best_price_date = i
            
                k = 1
                while  len(prices) - k > best_price_date:
                    
                    sell_price = prices[len(prices) - k]
                    profit = sell_price - best_price
                    print(best_price, sell_price, profit)
                    if profit > max_profit:
                        max_profit = max(profit, max_profit)
                    k+=1


                 

            
            
        return max_profit