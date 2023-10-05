class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totes = sum(nums)
        if totes % 2 == 1:
            return False

        tar = totes // 2
        dp = [False] * (tar + 1)

        dp[0] = True

        for num in nums:
            for cntdn in range(tar, num - 1, -1):
                dp[cntdn] = dp[cntdn] or dp[cntdn - num]

        return dp[tar]