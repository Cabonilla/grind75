class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return cntr[0][0]