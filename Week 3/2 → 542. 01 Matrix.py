class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        lr = len(mat)
        lc = len(mat[0])
        bnk = []

        for r in range(lr):
            for c in range(lc):
                if mat[r][c] == 0:
                    bnk.append((r,c))
                else:
                    mat[r][c] = "*"

        def dfs(r, c):
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]

            for r, c in bnk:
                for x,y in dirs:
                    nr = x + r
                    nc = y + c
                    if 0<=nr<lr and 0<=nc<lc and mat[nr][nc] == "*":
                        mat[nr][nc] = mat[r][c] + 1
                        bnk.append((nr, nc))

        dfs(0,0)
        return mat