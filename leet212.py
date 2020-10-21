212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        M, N = len(board), len(board[0])
        ret = []
        for word in words:
            path = [[1]*N for i in range(M)]
            flag = False
            for row in range(M):
                for col in range(N):
                    if board[row][col] == word[0]:
                        path[row][col] = 0
                        self.dfs(board, word, 1, path, row, col, flag, ret)
                        path[row][col] = 1
                        if ret and ret[-1] == word:
                            break
        return ret
        
    def dfs(self, board, word, idx, path, row, col, flag, ret):
        if idx == len(word):
            flag = True
            ret.append(word)
            return 
        M, N = len(board), len(board[0])
        if row + 1 < M and path[row+1][col] and board[row+1][col] == word[idx]:
            path[row+1][col] = 0
            self.dfs(board, word, idx+1, path, row+1, col, flag, ret)
            if flag :  return
            path[row+1][col] = 1
        if row - 1 >= 0 and path[row-1][col] and board[row-1][col] == word[idx]:
            path[row-1][col] = 0
            self.dfs(board, word, idx+1, path, row-1, col, flag, ret)
            if flag:   return
            path[row-1][col] = 1
        if col + 1 < N and path[row][col+1] and board[row][col+1] == word[idx]:
            path[row][col+1] = 0
            self.dfs(board, word, idx+1,path, row, col +1, flag, ret)
            if flag:   return
            path[row][col+1] = 1
        if col - 1 >= 0 and path[row][col-1] and board[row][col-1] == word[idx]:
            path[row][col-1] = 0
            self.dfs(board, word, idx+1, path, row, col-1, flag, ret)
            if flag:   return
            path[row][col-1] = 1