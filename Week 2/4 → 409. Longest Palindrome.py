class Solution:
    def longestPalindrome(self, s: str) -> int:
        cntr = Counter(s)
        sngl = False
        cnt = 0

        for i in cntr.keys():
            if cntr[i] % 2 == 0:
                cnt += cntr[i]
            else:
                cnt += cntr[i] - 1
                sngl = True

        return cnt + sngl
