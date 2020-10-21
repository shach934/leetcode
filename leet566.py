# 566. Reshape the Matrix

# In MATLAB, there is a very useful function called 'reshape', 
# which can reshape a matrix into a new one with different 
# size but keep its original data.

# You're given a matrix represented by a two-dimensional array, 
# and two positive integers r and c representing the row number 
# and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements 
# of the original matrix in the same row-traversing order as they were.

# If the 'reshape' operation with given parameters is possible 
# and legal, output the new reshaped matrix; Otherwise, 
# output the original matrix.

# Example 1:
# Input: 
# nums = 
# [[1,2],
 # [3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix 
# is a 1 * 4 matrix, fill it row by row by using the previous list.
# Example 2:
# Input: 
# nums = 
# [[1,2],
 # [3,4]]
# r = 2, c = 4
# Output: 
# [[1,2],
 # [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. 
# So output the original matrix.
# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = []
        for i in nums:
            flat.extend(i)
        print(flat)
        if(len(flat) != r*c):
            return nums
        else:
            ret = []
            idx = 0
            for j in range(r):
                ret.append(flat[idx:idx+c])
                idx = idx + c
        return ret
        
# 这个会快那么一点点，省去了先把矩阵铺平的步骤


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        M, N = len(nums), len(nums[0])
        ret = []
        if M*N != r*c:
            return nums
        i = 0
        while i < M * N:
            row = []
            for idx in range(c):
                row.append(nums[i//N][i - (i//N)*N])
                i += 1
            ret += row,
        return ret