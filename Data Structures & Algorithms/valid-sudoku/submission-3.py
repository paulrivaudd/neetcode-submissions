class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                keys = (("row", r, v), ("col", c, v), ("box", r // 3, c // 3, v))
                for k in keys:
                    if k in seen:
                        return False
                    seen.add(k)
        return True