class Solution:
    def myAtoi(self, s: str) -> int:
        minnum, maxnum = -2 ** 31, (2 ** 31) - 1
        hd, tl = 0, len(s)

        while hd < tl and s[hd] == ' ':
            hd += 1

        pos, neg = 0, 0

        if hd < tl and s[hd] == "+":
            pos += 1
            hd += 1
        if hd < tl and s[hd] == "-":
            neg += 1
            hd += 1

        res = 0.0
        while hd < tl and '0' <= s[hd] <= '9':
            res = res * 10 + (ord(s[hd]) - ord('0'))
            hd += 1

        if neg > 0:
            res = -res
        if pos > 0 and neg > 0:
            return 0

        if res < minnum:
            return minnum
        if res > maxnum:
            return maxnum

        return int(res)