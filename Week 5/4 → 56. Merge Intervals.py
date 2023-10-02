class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        bnk = []

        for x,y in sorted(intervals):
            # The second value of the last must be less than the current beginning, or else we need to merge.
            if not bnk or bnk[-1][1] < x:
                bnk.append([x,y])
            else:
                bnk[-1][1] = max(bnk[-1][1], y)

        return bnk