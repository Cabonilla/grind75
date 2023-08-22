class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        lr = len(image)
        lc = len(image[0])

        chngd = image[sr][sc]

        if chngd == color:
            return image

        def dfs(r, c):
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            image[r][c] = color

            for x, y in dirs:
                nr = x + r
                nc = y + c

                if 0<=nr<lr and 0<=nc<lc:
                    if image[nr][nc] == chngd:
                        dfs(nr, nc)

        dfs(sr,sc)
        return image