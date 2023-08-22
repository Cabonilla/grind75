class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(arr, tar):
            hd, tl = 0, len(arr) - 1

            while hd <= tl:
                md = (hd + tl) // 2
                if arr[md] == target:
                    return md
                elif arr[md] > target:
                    tl = md - 1
                else:
                    hd = md + 1

            return -1

        return bs(nums, target)