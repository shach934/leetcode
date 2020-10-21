718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

注意，dp，并非是一个最长公共子序列的问题。是必须要连续的才算。所以不能写：
if A[i-1] != B[j-1]:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
因为必须连续，如果不相等，直接就断掉了。就是0了

巧妙的地方在于用空间换时间，用多了一行一列来避免单独处理 也导致了A[i-1][j-1] 而不是A[i][j]

对于A[i][j] 和B[i][j] 如果他们相同，那么说明他们是当前的相同的子序列的最后一个元素，那么就能把这个元素从两个
序列中都剔除出去，剩下A[i-1][j-1] and B[i-1][j-1]。dp记录前一个的状态，可以直接转移到当前的状态了就。
而与前面的无关。
如果是要找到最长公共子序列，不要求连续的话，那么就要加上上面的那一行。

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        M, N = len(A), len(B)
        dp = [[0]*(N+1) for i in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max([max(row) for row in dp])