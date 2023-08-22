class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsm = 0
        mxsb = nums[0]

        for i in nums:
            if mxsm < 0:
                mxsm = 0

            mxsm += i
            mxsb = max(mxsb, mxsm)

        return mxsb