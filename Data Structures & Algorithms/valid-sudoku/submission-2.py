class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        col=defaultdict(set)
        boxes=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                val=board[r][c]
                if val=='.':
                    continue 
                b = (r // 3, c // 3)
                if val in rows[r] or val in col[c] or val in boxes[b]:
                    return False
                else:  
                    rows[r].add(board[r][c])
                    col[c].add(board[r][c])
                    boxes[b].add(board[r][c])
        return True  
                