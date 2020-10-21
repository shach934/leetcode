326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

如果不想用循环或者递归的话，
根据这个指数函数，就可以用log3（n）是个整数的话，就是3的指数
用log10（3）来实现log3.
或者更简单，把所有小于2**32的3的指数保存下来，看看是不是里面的数就好了。
或者把最大的小于2**32的数保存下来 然后去检查这个数能不能整除n，如果能够整除，说明一定是3的指数
    这是因为这个数的因子只有3 和3的各种倍数，因为是通过3的指数来的，里面混不进去别的因子，
    只要整除，除数肯定也是3的指数

后面想不到，但是log的方法应该能够想到才对啊，因为指数和log本来就是一对儿
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False