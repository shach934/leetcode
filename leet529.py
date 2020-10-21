529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
Example 1:
Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:
The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.



class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        M, N = len(board), len(board[0])
        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        import Queue
        que = Queue.Queue()
        que.put((row, col))
        record = {(row,col):1}
        while not que.empty():
            row, col = que.get()
            mines = 0
            for i in range(max(0, row-1), min(row+2, M)):
                for j in range(max(0, col-1), min(col+2, N)):
                    if board[i][j] == 'M':
                        mines += 1
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                if row-1>=0 and col-1>=0 and board[row-1][col-1] == 'E' and (row-1, col-1) not in record:
                    que.put((row-1, col-1))
                    record[(row-1,col-1)] = 1
                if row-1>=0 and board[row-1][col] == 'E' and (row-1, col) not in record:
                    que.put((row-1, col))
                    record[(row-1,col)] = 1
                if row-1>=0 and col+1<N and board[row-1][col+1] == 'E' and (row-1, col+1) not in record:
                    que.put((row-1, col+1))
                    record[(row-1, col+1)] = 1
                if row+1<M and board[row+1][col] == 'E' and (row+1, col) not in record:
                    que.put((row+1,col))
                    record[(row+1, col)] = 1
                if row+1<M and col+1<N and board[row+1][col+1] == 'E' and (row+1,col+1) not in record:
                    que.put((row+1, col+1))
                    record[(row+1, col+1)] = 1
                if row+1<M and col-1>=0 and board[row+1][col-1] == 'E' and (row+1, col-1) not in record:
                    que.put((row+1, col-1))
                    record[(row+1, col-1)] = 1
                if col-1>=0 and board[row][col-1] =='E' and (row, col-1) not in record:
                    que.put((row, col-1))
                    record[(row, col-1)] = 1
                if col+1<N and board[row][col+1] == 'E' and (row, col+1) not in record:
                    que.put((row, col+1))
                    record[(row, col+1)] = 1
        return board