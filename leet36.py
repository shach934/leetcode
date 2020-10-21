36. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


[[".","8","7","6","5","4","3","2","1"],
 ["2",".",".",".",".",".",".",".","."],
 ["3",".",".",".",".",".",".",".","."],
 ["4",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".",".","."],
 ["6",".",".",".",".",".",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 ["8",".",".",".",".",".",".",".","."],
 ["9",".",".",".",".",".",".",".","."]]

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows, cols, squares = [{} for i in range(9)], [{} for i in range(9)], [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[3*(i/3) + j/3]:
                        return False
                    else:
                        rows[i][board[i][j]] = 1
                        cols[j][board[i][j]] = 1
                        squares[3*(i/3) + j/3][board[i][j]] = 1
        return True