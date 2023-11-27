class MedianFinder:

    def __init__(self):
        self.bnk = []

    def addNum(self, num: int) -> None:
        if not self.bnk:
            self.bnk.append(num)
        else:
            idx = bisect_left(self.bnk, num)
            self.bnk.insert(idx, num)

    def findMedian(self) -> float:
        slen = len(self.bnk) - 1
        if slen % 2 == 0:
            return self.bnk[slen // 2]
        else:
            return (self.bnk[slen // 2] + self.bnk[slen // 2 + 1]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()