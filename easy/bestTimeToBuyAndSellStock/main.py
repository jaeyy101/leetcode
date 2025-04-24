class Solution:
    def maxProfit(self, prices: list[int]) -> bool:
        cheapestPrice = float("inf")
        maxProfit = 0

        for price in prices:
            if price < cheapestPrice:
                cheapestPrice = price
                continue

            currentProfit = price - cheapestPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit

        return maxProfit
    
s = Solution()
print(s.maxProfit([1,6,4,3,7]))