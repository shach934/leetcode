# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        width, height = len(grid[0]), len(grid)
        num = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    num += 1
                    grid = self.erease(grid, i,  j)
        return num
        
    def erease(self, grid, i, j):
        queue = [(i,j)]
        width, height = len(grid[0]), len(grid)
        while queue:
            i, j = queue[0]
            grid[i][j] = '0'
            if i+1<height and grid[i+1][j] == '1':
                queue.append((i+1,j))
                grid[i+1][j] = '0'
            if i-1>=0 and grid[i-1][j] == '1':
                queue.append((i-1, j))
                grid[i-1][j] = '0'
            if j-1 >=0 and grid[i][j-1] == '1':
                queue.append((i,j-1))
                grid[i][j-1]= '0'
            if j+1<width and grid[i][j+1] == '1':
                queue.append((i,j+1))
                grid[i][j+1]= '0'
            queue.pop(0)
        return grid