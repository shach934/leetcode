753. Cracking the Safe

There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int  the number of digits. 
        :type k: int  option 0,1,..., k-1
        :rtype: str
        """

        # 没有能够找到证明，但是从0^k出发，然后每次都重用最后n-1个数字，总能构建出来一个string符合标准。 长度一定是 n - 1 + k**n, dfs找到这个string即可。
        # 这道题的证明其实很简单，其实就是一个欧拉路径。欧拉路径指的是 在一个图中，过每个边且只过一次的路径。
        # 有向图而言，要求每个节点的入度和出度一样的。
        # 无向图而言，要求每个节点的度为偶数。
        # 两种情况下，都要求图为联通图。

        # n = 2, k = 2, 节点为四个 00， 01， 11， 10， 边为 00->01, 01->11 01->10. 11->10. 10->00. 10->01
        # 每个节点都连接顶针的节点，每个节点在0和1位出现的概率是相同的，所以保证了出度和入度相同，一定存在欧拉路径。
        # 即一定能够从一个点出发，过且仅过每个节点一次，形成一个字符串，保证每移一位就是一个valid的字符
        # dfs从任一节点出发，找到这个路径，
        
        def dfs(n, k, seen, curr):
            if len(seen) == k ** n:
                return curr
            L = len(curr)
            for i in range(k-1, -1, -1):
                next_Op = curr[L-n+1:] + str(i)
                if next_Op not in seen:
                    seen[next_Op] = 1
                    ans = dfs(n, k, seen, curr + str(i))
                    if ans:
                        return ans
                    else:
                        del seen[next_Op]
        start = '0'*n
        seen ={start: 1}
        return dfs(n, k, seen, start)