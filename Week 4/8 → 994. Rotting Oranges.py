class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        lr, lc = len(grid), len(grid[0])
        empt, frsh, rott = 0,1,2
        frshcnt = 0
        hr = 0

        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == frsh:
                    frshcnt += 1
                elif grid[r][c] == rott:
                    q.append([r,c])

        dirs = ([0,1], [1,0], [0,-1], [-1,0])

        while q and frshcnt > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for x, y in dirs:
                    nr = r + x
                    nc = c + y
                    if (0 > nr or nr >= lr) or (0 > nc or nc >= lc) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    frshcnt -= 1
            hr += 1

        return hr if frshcnt == 0 else -1

            