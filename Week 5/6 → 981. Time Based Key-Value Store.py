class TimeMap:

    def __init__(self):
        self.tmbnk = collections.defaultdict(list)
        self.valbnk = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmbnk[key].append(timestamp)
        self.valbnk[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.valbnk.keys():
            return ""

        if timestamp >= self.tmbnk[key][-1]:
            return self.valbnk[key][-1]

        # BS search through timestamps.
        hd, tl = 0, len(self.tmbnk[key]) - 1
        ans = -1
        while hd <= tl:
            md = (hd + tl) // 2
            if self.tmbnk[key][md] <= timestamp:
                ans = md
                hd = md + 1
            else:
                tl = md - 1

        if ans < 0:
            return ""
        else:
            return self.valbnk[key][ans]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)