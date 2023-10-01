class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtrakcing
        # If past tar, onto the next.
        bnk = []
        lc = len(candidates)

        # Best to use a tree approach like DFS.
        def dfs(cur, sm, i):
            if sm > target:
                return target

            if sm == target:
                bnk.append(cur)

            for i in range(i, lc):
                # running totes
                dfs(cur + [candidates[i]], sm + candidates[i], i)

        dfs([], 0, 0)
        return bnk
