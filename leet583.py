583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M, N = len(word1), len(word2)
        matrix = [[0]*(N+1) for i in range(M+1)]
        for i in range(1, N+1):
            matrix[0][i] = i
        for i in range(1, M+1):
            matrix[i][0] = i
        for i in range(1, M+1):
            for j in range(1, N+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1
        return matrix[M][N]