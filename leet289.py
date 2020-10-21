289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                lives = self.aroundLife(board, i, j)
                print(lives)
                if board[i][j] and lives <= 3 and lives >= 2:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(M):
            for j in range(N):
                board[i][j] >>= 1        
        
    def aroundLife(self, board, i, j):
        M, N = len(board), len(board[0])
        count = 0
        if i - 1 >= 0 and j - 1 >= 0:   count += board[i-1][j-1]&1
        if i - 1 >= 0:                  count += board[i-1][j]&1
        if i - 1 >= 0 and j + 1 < N:    count += board[i-1][j+1]&1
        if j - 1 >= 0:                  count += board[i][j-1] & 1
        if j + 1 < N:                   count += board[i][j+1]&1
        if i + 1 < M and j - 1 >= 0:    count += board[i+1][j-1] & 1
        if i + 1 < M:                   count += board[i+1][j] & 1
        if i + 1 < M and j + 1 < N:     count += board[i+1][j+1] & 1
        return count
        
这个是按照最开始的想法， 先加上一行，然后再加上一列，每个格子的最终状态存到格子的左上角去。然后把加的一行
和一列删除掉。但是这个并不是真正的inplace，在python里面也不能保存下来结果，因为经过了复制过程。地址完全改变了
        
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        firstR = [0]*N
        board = [firstR] + board
        for i in range(M+1):
            board[i] = [0] + board[i]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                lives = self.aroundLife(board,i,j)
                if board[i][j] == 0 and lives == 3:
                    board[i-1][j-1] = 1
                elif board[i][j] == 1 and lives <=3 and lives >= 2:
                    board[i-1][j-1] = 1
                else:
                    board[i-1][j-1] = 0
        board.pop()
        for i in range(M):
            board[i].pop()