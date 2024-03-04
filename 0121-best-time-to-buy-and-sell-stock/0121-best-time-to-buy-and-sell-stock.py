class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > profit:
                profit = prices[i] - lowest
        
        return profit
        
        
        
        