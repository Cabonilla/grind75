from types import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sched = sorted(zip(startTime, endTime, profit))
        lj = len(sched)

        startTime.sort()
        print(sched)

        dp = [0 for _ in range(lj + 1)]

        for i in range(lj - 1, -1, -1):
            plc = bisect.bisect_left(startTime, sched[i][1])
            dp[i] = max(dp[i + 1], dp[plc] + sched[i][2])

        return dp[0]    
        