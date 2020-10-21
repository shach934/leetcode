64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to 
bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if i - 1 >=0 and j - 1>= 0:
                    grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
                elif i-1>=0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif j-1>=0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
        return grid[M-1][N-1]