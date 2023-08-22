class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bnk = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                bnk.append(interval)
            elif newInterval[1] < interval[0]:
                bnk.append(newInterval)
                newInterval = interval
            elif newInterval[0] <= interval[1] or interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        bnk.append(newInterval)
        return bnk