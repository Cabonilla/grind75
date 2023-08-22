class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = prices[0]
        maxp = 0

        for i in range(len(prices)):
            minv = min(minv, prices[i])
            maxp = max(maxp, prices[i] - minv)

        return maxp