class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 1:
            return 0
        
        cheapestPrice = prices[0]
        maxProfit = 0

        n = len(prices)
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                if i == n-1:
                    maxProfit += prices[i] - cheapestPrice
            else:
                maxProfit += prices[i-1] - cheapestPrice
                cheapestPrice = prices[i]

        return maxProfit
    

s = Solution()
print(s.maxProfit([1,2,3]))
