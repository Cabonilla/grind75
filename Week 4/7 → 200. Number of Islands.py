class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        islands = 0

        if not grid:
            return 0

        def dfs(r,c):
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]

            if 0 > r or r >= lr or 0 > c or c >= lc or grid[r][c] != '1':
                return

            grid[r][c] = '0'

            for x, y in dirs:
                nr = x + r
                nc = y + c
                dfs(nr, nc)

        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands

