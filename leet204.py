204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

一个一个的去判断肯定很慢，最好是挨个的去踩，但是如果是数字去踩，然后再去判断能否整除，就又多余了
直接用index就行，每隔当前prime个就直接弄成false，比处理数字快很多

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        nums = [True] * n
        nums[:2] =  [False, False]
        for i in range(2, int(n**0.5)+1):
            if nums[i]:
                nums[i*i::i] = [False] * len(nums[i*i::i])
        return sum(nums)