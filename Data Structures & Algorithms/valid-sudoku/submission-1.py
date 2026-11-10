class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            row_vals = set()
            for val in range(9):
                if board[row][val] == '.':
                    continue
                if board[row][val] in row_vals:
                    return False;
                row_vals.add(board[row][val])

        for col in range(len(board)):
            col_vals = set()
            for val in range(9):
                if board[val][col] == '.':
                    continue
                if board[val][col] in col_vals:
                    return False;
                col_vals.add(board[val][col])

        for boxRow in range(0,9,3):
            for boxCol in range(0,9,3):
                box_vals = set()
                for x in range(3):
                    for y in range(3):
                        if board[boxRow+x][boxCol+y] == '.':
                            continue
                        if board[boxRow+x][boxCol+y] in box_vals:
                            return False;
                        box_vals.add(board[boxRow+x][boxCol+y])
        return True

