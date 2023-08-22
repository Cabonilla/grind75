# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lw, hg = 1, n

        while lw <= hg:
            md = (lw + hg) // 2

            if isBadVersion(md):
                hg = md - 1
            else:
                lw = md + 1

        return lw