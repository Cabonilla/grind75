class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lr = len(board)
        lc = len(board[0])
        dirs = [(0,-1), (-1, 0), (0, 1), (1, 0)]

        def dfs(r, c, idx, seen):
            if board[r][c] == word[idx]:
                if idx == len(word) - 1:
                    return True

                for x, y in dirs:
                    nr, nc = r + x, c + y
                    if 0 <= nr < lr and 0 <= nc < lc and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        if dfs(nr, nc, idx + 1, seen) == True:
                            return True
                        seen.remove((nr, nc))

            return False

        for r in range(lr):
            for c in range(lc):
                if dfs(r, c, 0, {(r, c)}):
                    return True

        return False