class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        prof = 0
        for i in range(0, len(prices)):
            buy = min(buy, prices[i])
            prof = max(prof, prices[i] - buy)

        return prof