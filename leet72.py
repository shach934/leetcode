72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        M, N = len(word1), len(word2)
        matrix = [[0]*(N+1) for i in range(M+1)]
        for i in range(1, M+1):
            matrix[i][0] = i
        for j in range(1, N+1):
            matrix[0][j] = j
        for i in range(1, M+1):
            for j in range(1, N+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min([matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]]) + 1
        return matrix[M][N]