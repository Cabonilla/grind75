class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [-1]
        heights.append(0)

        tllst = -1
        mxarea = 0

        for x in range(len(heights)):
            y = heights[x]
            while heights[stk[tllst]] > y:
                h = heights[stk.pop()]
                w = x - stk[tllst] - 1
                
                mxarea = max(mxarea, h * w)

            stk.append(x)

        return mxarea
