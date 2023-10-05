class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        mxpal = ''

        def verify_pal(str, hd, tl):
            while hd >= 0 and tl < ls and str[hd] == str[tl]:
                hd -= 1
                tl += 1
            return str[hd + 1:tl]

        for i in range(ls):
            odd_pal = verify_pal(s, i, i)
            even_pal = verify_pal(s, i, i + 1)
            mxpal = max([mxpal, odd_pal, even_pal], key=len)

        return mxpal