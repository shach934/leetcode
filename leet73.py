73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # store if a coloum or a crow has zero in the first position.
        
        M, N = len(matrix), len(matrix[0])
        firstR, firstC = False, False
        for i in range(M):
            if matrix[i][0] == 0:
                firstC = True
                break
        for i in range(N):
            if matrix[0][i] == 0:
                firstR = True
                break

        for i in range(1,M):
            for j in range(1,N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1,M):
            if matrix[i][0] == 0:
                for j in range(1,N):
                    matrix[i][j] = 0
        for i in range(1,N):
            if matrix[0][i] == 0:
                for j in range(1,M):
                    matrix[j][i] = 0
                    
        if firstR:
            for i in range(N):
                matrix[0][i] = 0
        if firstC:
            for i in range(M):
                matrix[i][0] = 0