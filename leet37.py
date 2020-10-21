"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

[[".",".","9","7","4","8",".",".","."],
 ["7",".",".",".",".",".",".",".","."],
 [".","2",".","1",".","9",".",".","."],
 [".",".","7",".",".",".","2","4","."],
 [".","6","4",".","1",".","5","9","."],
 [".","9","8",".",".",".","3",".","."],
 [".",".",".","8",".","3",".","2","."],
 [".",".",".",".",".",".",".",".","6"],
 [".",".",".","2","7","5","9",".","."]]

You may assume that there will be only one unique solution.
"""

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = [{i+1:0 for i in range(9)} for j in range(9)]
        cols = [{i+1:0 for i in range(9)} for j in range(9)]
        squares = [{i+1:0 for i in range(9)} for j in range(9)]
        stack = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    stack.append((i,j))
                else:
                    num = int(board[i][j])
                    rows[i][num] = 1
                    cols[j][num] = 1
                    squares[3*(i//3) + j//3][num] = 1
        go = [True]          
        self.helper(board, stack, rows, cols, squares, go)
    
    def helper(self, board, stack, rows, cols, squares, go):
        if len(stack) == 0:
            go[0] = False
            return 
        r, c = stack.pop()
        for i in range(1,10):
            if not rows[r][i] and not cols[c][i] and not squares[3*(r//3)+c//3][i]:
                board[r][c] = str(i)
                rows[r][i] = 1
                cols[c][i] = 1
                squares[3*(r//3)+c//3][i] = 1
                self.helper(board, stack, rows, cols, squares, go)
                if go[0]:
                    board[r][c] = '.'
                    rows[r][i] = 0
                    cols[c][i] = 0
                    squares[3*(r//3)+c//3][i] = 0
                else:
                    return 
        stack.append((r,c))