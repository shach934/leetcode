542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(matrix, row, col):
            M, N = len(matrix), len(matrix[0])
            level = {(row, col):0}
            # parent = {(row, col): None}
            count = 1
            frontier = [(row,col)]
            while frontier:
                nextL = []
                for node in frontier:
                    if node[0] + 1 < M and (node[0]+1, node[1]) not in level:
                        if matrix[node[0]+1][node[1]]:
                            nextL.append((node[0]+1, node[1]))
                            level[(node[0]+1, node[1])] = count
                        else:
                            return count
                    if node[1] + 1 < N and (node[0], node[1] + 1) not in level:
                        if matrix[node[0]][node[1]+1]:
                            nextL.append((node[0], node[1]+1))
                            level[(node[0], node[1] + 1)] = count
                        else:
                            return count
                    if node[0] - 1 >- 1 and (node[0]-1, node[1]) not in level:
                        if matrix[node[0]-1][node[1]]:
                            nextL.append((node[0]-1, node[1]))
                            level[(node[0]-1,node[1])] = count
                        else:
                            return count
                    if node[1] - 1 > -1 and (node[0], node[1]-1) not in level:
                        if matrix[node[0]][node[1]-1]:
                            nextL.append((node[0], node[1]-1))
                            level[(node[0], node[1]-1)] = count
                        else:
                            return count
                count += 1
                frontier = nextL
                    
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1:
                    matrix[i][j] = bfs(matrix, i, j)
        return matrix