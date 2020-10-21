661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image, you need to design 
a smoother to make the gray scale of each cell becomes the average gray scale 
(rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 
surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(M), len(M[0])
        newImg = [[0 for i in range(col)] for j in range(row)]
        move = [-1, 0, 1]
        for i in range(row):
            for j in range(col):
                summ, num = 0, 0
                for m in move:
                    for n in move:
                        if i + m <row and i + m> -1 and j  + n < col and j + n > -1:
                            summ += M[i+m][j+n]
                            num += 1
                newImg[i][j] = summ//num
        return newImg