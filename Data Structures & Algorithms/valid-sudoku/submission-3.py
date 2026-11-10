class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxs = {}

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box = (row//3, col//3)
                rows.setdefault(row, set())
                cols.setdefault(col, set())
                boxs.setdefault(box, set())
                if val in rows[row] or val in cols[col] or val in  boxs[box]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxs[box].add(val)
        return True

                
                