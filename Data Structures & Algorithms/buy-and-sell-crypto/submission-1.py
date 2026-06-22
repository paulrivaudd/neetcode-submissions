class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n < 2: return 0
        min_price = prices[0]
        profit = 0
        for k in range(1, n):
            if prices[k] < min_price:
                min_price = prices[k]
            elif prices[k] - min_price > profit:
                profit = prices[k] - min_price
        return profit