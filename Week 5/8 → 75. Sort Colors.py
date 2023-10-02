class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers
        lw, hg = 0, len(nums) - 1
        plc = 0

        while plc <= hg:
            if nums[plc] == 0:
                # Swap
                nums[lw], nums[plc] = nums[plc], nums[lw]
                lw += 1
                plc += 1

            elif nums[plc] == 1:
                plc += 1

            else:
                # Swap
                nums[plc], nums[hg] = nums[hg], nums[plc]
                hg -= 1