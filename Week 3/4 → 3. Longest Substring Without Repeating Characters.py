class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hd, tl = 0,0
        mxln = 0
        mxstr = ''

        while tl < len(s):
            if s[tl] not in mxstr:
                mxstr += s[tl]
                tl += 1
                mxln = max(mxln, len(mxstr))
            else:
                hd += 1
                mxln = max(mxln, len(mxstr))
                mxstr = mxstr[1:]

        return mxln