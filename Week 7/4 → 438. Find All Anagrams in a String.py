class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        srtgrm = ''.join(sorted(p))
        win = ''
        idxs = []
        hd = 0

        for c in s:
            win += c
            if len(win) == len(srtgrm):
                if ''.join(sorted(win)) == srtgrm:
                    idxs.append(hd)
                win = win[1:]
                hd += 1

        return idxs
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dictp = collections.Counter(p)
        dicts = collections.Counter(s[:len(p)])
        bnk = []
        hd, tl = 0, len(p)

        while tl <= len(s):
            if dicts == dictp:
                bnk.append(hd)

            dicts[s[hd]] -= 1
            if dicts[s[hd]] <= 0:
                dicts.pop(s[hd])

            if tl < len(s):
                dicts[s[tl]] += 1

            tl += 1
            hd += 1

        return bnk