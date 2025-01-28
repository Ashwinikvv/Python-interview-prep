# Python Program to solve stock buy and sell 
# using one traversal

def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    # Update the minimum value seen so far 
    # if we see smaller
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])
        
        # Update result if we get more profit                
        res = max(res, prices[i] - minSoFar)
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))





# Python Program to solve stock buy and sell by  
# exploring all possible pairs

def max_profit(prices):
    n = len(prices)
    res = 0

    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))




from itertools import pairwise  # Importing the pairwise function from itertools module

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize total profit to zero
        total_profit = 0
      
        # Loop through each pair of successive prices using pairwise()
        for buy_price, sell_price in pairwise(prices):
            # Calculate profit for the current pair
            # If sell price is greater than buy price, add the difference to total profit
            # Otherwise, add zero (no loss, no gain)
            profit = max(0, sell_price - buy_price)
            total_profit += profit
      
        # Return the total calculated profit
        return total_profit
