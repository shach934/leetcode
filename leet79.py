79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are 
those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


[["C","A","A"],
 ["A","A","A"],
 ["B","C","D"]]
"AAB"

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        path = [[1]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    path[i][j] = 0
                    if self.backtrack(board, word, 1, path, i, j):
                        return True
                    else:
                        path[i][j] = 1
        return False

    def backtrack(self, board, word, n, path, i, j):
        if len(word) == n:
            return True
        row, col = len(board), len(board[0])
        if i + 1 < row and board[i + 1] [j] == word[n] and path[i+1][j]:
            path[i+1][j] = 0
            if self.backtrack(board, word, n+1, path, i + 1, j):
                return True
            else:
                path[i+1][j] = 1
        if i - 1 >= 0 and board[i-1][j] == word[n] and path[i-1][j]:
            path[i-1][j] = 0
            if self.backtrack(board, word, n+1, path, i-1, j):
                return True
            else:
                path[i-1][j] = 1
        if j - 1 >= 0 and board[i][j-1] == word[n] and path[i][j-1]:
            path[i][j-1] = 0
            if self.backtrack(board, word, n+1, path, i, j-1):
                return True
            else:
                path[i][j-1] = 1
        if j + 1 < col and board[i][j+1] == word[n] and path[i][j+1]:
            path[i][j+1] = 0
            if self.backtrack(board, word, n+1, path, i, j+1):
                return True
            else:
                path[i][j+1] = 1
        return False