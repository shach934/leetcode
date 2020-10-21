507. Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

只需要检查到sqrt(num)就可以了，不需要检查到num本身或者num除以2.
因为大于sqrt（num）的数在num除以之前小数的时候肯定出现过了！就不用重复计算了

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        mydict, currsum = {}, 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 :
                currsum += i + num/i
                print(i, num/i)
        if int(num**0.5) * int(num**0.5)==num :
            currsum -= int(num**0.5)
        if currsum == num:
            return True
        else:
            return False