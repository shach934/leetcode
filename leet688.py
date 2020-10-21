688. Knight Probability in Chessboard

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int size of board N x N
        :type K: int number of moves
        :type r: int start row
        :type c: int start col
        :rtype: float
        """
        rem = {}
        moves = [(1,2),(1,-2),(-1,2),(-1,-2),(-2, -1),(-2,1),(2,-1),(2,1)]
        
        def in_board(N, r, c):
            return 0 <= r < N and 0 <= c < N

        def dfs(N, K, r, c):

            if K == 0 and in_board(N, r, c):
                return 1
            if not in_board(N, r, c):
                return 0

            if (K, r, c) in rem:
                return rem[(K, r, c)]
            count = 0.0
            for move in moves:
                prob = dfs(N, K - 1, r + move[0], c + move[1])
                rem[(K - 1, r + move[0], c + move[1])] = prob
                count += prob / 8.0
            rem[(K, r, c)] = count
            return rem[(K, r, c)]

        return dfs(N, K, r, c)
