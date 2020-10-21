'''
695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. 
(If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, 
because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

# 宽优搜索，beat 99.16% 哈哈

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxA = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area, grid = self.broadSearch(grid, i, j)
                    maxA = max(area,maxA)
        return maxA
        
    def broadSearch(self, grid, i, j):
        height, width, area = len(grid), len(grid[0]), 1
        queue = [(i,j)]
        grid[i][j] = 0
        while queue:
            i, j = queue[0]
            if i + 1 < height and grid[i+1][j]:
                queue.append((i+1,j))
                grid[i+1][j] = 0
                area += 1
            if i - 1 >= 0 and grid[i-1][j]:
                queue.append((i-1,j))
                grid[i-1][j] = 0
                area += 1
            if j - 1 >= 0 and grid[i][j-1]:
                queue.append((i,j-1))
                grid[i][j-1] = 0
                area += 1
            if j + 1 < width and grid[i][j+1]:
                queue.append((i,j+1))
                grid[i][j+1] = 0
                area += 1
            queue.pop(0)
        return area, grid