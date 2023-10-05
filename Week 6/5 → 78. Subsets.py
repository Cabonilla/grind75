class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        init = [[]]
        for j in nums:
            init += [i + [j] for i in init]
        return init

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        res = []

        def bktrk(res, strt, sbst, nm):
            res.append(list(sbst))
            for i in range(strt, ln):
                sbst.append(nums[i])
                bktrk(res, i + 1, sbst, nums)
                sbst.pop()

        bktrk(res, 0, [], nums)

        return res