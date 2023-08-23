class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        lft = [1] * ln
        rgt = [1] * ln

        for i in range(1, ln):
            lft[i] = lft[i - 1] * nums[i - 1]
        for j in range(ln - 2, -1, -1):
            rgt[j] = rgt[j + 1] * nums[j + 1]

        return [lft[i] * rgt[i] for i in range(ln)]