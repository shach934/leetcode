# 526. Beautiful Arrangement

# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?

# Example 1:
# Input: 2
# Output: 2
# Explanation: 

# The first beautiful arrangement is [1, 2]:

# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

# The second beautiful arrangement is [2, 1]:

# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.

# 还是会超时，应该改成不要每次去检查，而是把用过的直接踢出去 可能会快
# 在函数内部修改变量数值，如果不返回的话，是无效的，
# 如果想要把变量修改值传回去的话，那就要用list或者弄个object这种可以修改的变量才行
# 还有list在内部添加一个新的list也是不好使的，因为那个新的list变量出去就变了，要值拷贝过去

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = []
        count = [0]
        self.fillN(num, N, count)
        return count[0]
        
    def fillN(self, num, N, count):
        if len(num) == N:
            count[0] += 1
            return 
        for i in range(1, N+1):
            flag = True
            for j in num:
                if i == j:
                    flag = False
            if flag and (i%(len(num)+1) == 0 or (len(num)+1)%i == 0):
                num.append(i)
                fillN(num, N, count)
                num.pop()
        return 

# 回头再写吧。。。。。
                num = []
        count = [0]
        self.fillN(num, N, count)
        return count[0]
        
    def fillN2(self, num, N, count):
        if len(num) == N:
            count[0] += 1
            return 
        for i in range(1, N+1):
            
            if flag and (i%(len(num)+1) == 0 or (len(num)+1)%i == 0):
                num.append(i)
                fillN(num, N, count)
                num.pop()
        return 
        