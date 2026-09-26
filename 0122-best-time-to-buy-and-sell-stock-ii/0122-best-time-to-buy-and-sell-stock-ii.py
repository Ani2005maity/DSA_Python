class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prof = 0
        n = len(prices)
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                prof += (prices[i + 1] - prices[i])

        return prof