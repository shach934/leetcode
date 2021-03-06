773. Sliding Puzzle

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        #board 一定是2 x 3 array
        # 宽搜，每次移动一个，看看是否到了目标

        def findZero(board):
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0:
                        return (i, j)

        def formNode(board):
            return (tuple(board[0]), tuple(board[1]))

        def inBoard(i, j):
            return 0<=i<2 and 0<=j<3

        def swapTuple(node, a, b):
            k, l = a[0], a[1]
            m, n = b[0], b[1]
            newNode = []
            for i in range(2):
                row = []
                for j in range(3):
                    if i == k and j == l:
                        row.append(node[m][n])
                    elif i == m and j == n:
                        row.append(node[k][l])
                    else:
                        row.append(node[i][j])
                newNode.append(row)
            return (tuple(newNode[0]), tuple(newNode[1]))

        # tuple支持hashmap，但是不支持修改
        aim = ((1,2,3), (4,5,0))
        nodes = [formNode(board)]
        level = 1
        seen = {nodes[0]:0}
        while nodes :
            nextLevel = []
            for start in nodes:
                if start == aim:
                    return seen[start]
                zeros = findZero(start)
                moves = [[0,-1],[0,1],[1,0],[-1,0]]
                for i in range(4):
                    if inBoard(zeros[0] + moves[i][0], zeros[1] + moves[i][1]):
                        newNode = swapTuple(start, zeros, (zeros[0] + moves[i][0], zeros[1] + moves[i][1])) 
                        if newNode not in seen:
                            nextLevel.append(newNode)
                            seen[newNode] = level

            level += 1
            nodes = nextLevel[:]
        return -1