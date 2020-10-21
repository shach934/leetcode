576. Out of Boundary Paths

here is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int row of grid
        :type n: int col of grid
        :type N: int steps to move
        :type i: int start row
        :type j: int start col
        :rtype: int  paths
        """
        rem = {}
        
        def in_grid(m, n, i, j):
            return 0 <= i < m and 0 <= j < n
        
        def dfs(m, n, i, j, N):

            if N == 0 and in_grid(m, n, i, j):
                return 0

            if not in_grid(m,n,i,j):
                return 1

            if (i, j, N) in rem:
                return rem[(i, j, N)]

            up = dfs(m, n, i-1, j, N-1)
            rem[(i-1, j, N-1)] = up

            down = dfs(m, n, i+1, j, N-1) 
            rem[(i+1, j, N-1)] = down

            right = dfs(m, n, i, j+1, N-1)
            rem[(i, j+1, N-1)] = right

            left = dfs(m, n, i, j-1, N-1) 
            rem[(i, j-1, N-1)] = left

            rem[(i, j, N)] = up + down + left + right
            
            return rem[(i, j, N)]   
            
        return dfs(m, n, i, j, N)  % 1000000007   