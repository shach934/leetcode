119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowNow = [1]
        for i in range(1, rowIndex+1):
            rowNext = [1]
            for j in range(1, i):
                rowNext.append(rowNow[j] + rowNow[j-1])
            rowNext.append(1)
            rowNow = rowNext[:]
        return rowNow