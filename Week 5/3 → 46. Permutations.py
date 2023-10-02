from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

# Recursive approach would be best.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        bnk = []

        # Base cases.
        if len(nums) == 1:
            return [nums]

        elif len(nums) == 2:
            bnk.append(nums)
            bnk.append(nums[::-1])
            return bnk

        # Nested list w/ recursive iteration of values.
        else:
            nstbnk = []
            frst = nums[0]
            bnk = self.permute(nums[1:])
            print(bnk)
            # First + Rest
            for i in bnk:
                # Iterate over rest.
                for j in range(0, len(i) + 1):
                    perm = i[:j] + [frst] + i[j:]
                    nstbnk.append(perm)
            return nstbnk
