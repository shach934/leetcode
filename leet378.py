# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are 
# sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, 
# not the kth distinct element.

# Example:

# matrix = [
   # [ 1,  5,  9],
   # [10, 11, 13],
   # [12, 13, 15]
# ],
# k = 8,

# return 13.

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        mylist, n = [], len(matrix)
        while len(mylist) < k:
            small, idx = float('inf'), -1   
            for i in range(n):                  # 每次添加一个元素进去的话
                if matrix[i]:                   # 比较n次。所以其实是O(nk)
                    if matrix[i][0] < small:    # 严重怀疑是删除导致这么慢的
                        small = matrix[i][0] 
                        idx = i
            print(matrix)
            mylist.append(small)
            del matrix[idx][0]
        return mylist[-1]

# 我真是要吐血了，这个竟然比上面的要快得多。排序最快也要nlogn，竟然比上面的快？！
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = sum(matrix, [])
        m.sort()
        return m[k-1]