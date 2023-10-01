class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # BS search to look for pivot point.
        hd, tl = 0, len(nums) - 1
        while hd <= tl:
            mid = (hd + tl) // 2
            if nums[mid] == target:
                return mid
            
            if nums[hd] <= nums[mid]:
                # 4 5 6 7 0 1 2 
                # h     m t
                if nums[hd] <= target < nums[mid]:
                    tl = mid - 1
                else:
                    hd = mid + 1
            else:
                if nums[mid] < target <= nums[tl]:
                    hd = mid + 1
                else:
                    tl = mid - 1

        return -1


        