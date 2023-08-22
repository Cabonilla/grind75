class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            hd, tl = i + 1, len(nums) - 1
            tar = 0 - nums[i]
            while hd < tl:
                if nums[hd] + nums[tl] == tar:
                    ans.add((nums[i], nums[hd], nums[tl]))
                    hd += 1
                    tl -= 1
                elif nums[hd] + nums[tl] < tar:
                    hd += 1
                else:
                    tl -= 1

        return list(ans)