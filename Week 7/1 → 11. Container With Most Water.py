class Solution:
    def maxArea(self, height: List[int]) -> int:
        hd, tl = 0, len(height) - 1
        ans = 0
        while hd <= tl:
            area = min(height[hd], height[tl]) * (tl - hd)
            ans = max(ans, area)

            if height[hd] < height[tl]:
                hd += 1
            else:
                tl -= 1

        return ans