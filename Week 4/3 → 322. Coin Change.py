class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mxamnt = amount + 1
        dp = [mxamnt] * mxamnt
        dp[0] = 0

        for instc in range(1, mxamnt):
            for coin in coins:
                if instc - coin >= 0:
                    dp[instc] = min(dp[instc], dp[instc - coin] + 1)
        
        if dp[amount] != mxamnt:
            return dp[amount]
        else:
            return -1