class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sm = {}

        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in sm.keys():
                return [i, sm[tar]]
            sm[nums[i]] = i

        