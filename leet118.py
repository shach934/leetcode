118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(pascal[-1][j] + pascal[-1][j-1])
            row.append(1)
            pascal.append(row)
        return pascal