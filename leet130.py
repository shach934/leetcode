130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

import Queue
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not (len(board) and len(board[0])):
            return 
        count, record = [0], {} 
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    flag = self.dfs(board, i, j, count)
                    record[count[0]] = flag
                    count[0] += 1
        for i in range(M):
            for j in range(N):
                if board[i][j] != 'X':
                    if record[board[i][j]]:
                        board[i][j] = 'X'
                    else:
                        board[i][j] = 'O'
                        
    def dfs(self, board, row, col, count):
        flag = True
        M, N = len(board), len(board[0])
        que, record=Queue.Queue(), {}
        que.put((row, col))
        record[(row,col)] = 1
        while not que.empty():
            row, col = que.get_nowait()
            if row == 0 or row == M - 1 or col == 0 or col == N - 1:
                flag = False
            board[row][col] = count[0]
            if row + 1 < M and board[row+1][col] == 'O':
                if (row+1,col) not in record:
                    que.put_nowait((row+1, col))
                    record[(row+1,col)] = 1
            if row - 1 >=0 and board[row-1][col] == 'O':
                if (row-1,col) not in record:
                    que.put_nowait((row-1, col))
                    record[(row-1,col)] = 1
            if col + 1 < N and board[row][col+1] == 'O':
                if (row,col+1) not in record:
                    que.put_nowait((row, col+1))
                    record[(row,col+1)] = 1
            if col - 1 >=0 and board[row][col-1] == 'O':
                if (row, col-1) not in record:
                    que.put_nowait((row, col-1))
                    record[(row,col-1)] = 1
        return flag