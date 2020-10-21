306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def proceed(num, first, second):
            idx = len(first) + len(second)
            while idx < len(num):
                third = str(int(first) + int(second))
                if third == num[idx:idx+len(third)]:
                    if len(third) == 1 or (len(third) > 1 and third[0] != '0'):
                        idx += len(third)
                        first, second = second, third
                else:
                    return False
            if idx == len(num):
                return True
            else:
                return False
        
        first, second = '', ''
        for i in range(1, len(num)//2 + 1):
            first = num[:i]
            
            for j in range(i+1, len(num)):
                second = num[i:j]
                third = str(int(first) + int(second))
                if third == num[j:j+len(third)]:
                    if (len(first) == 1 or (len(first) > 1 and first[0] != '0')) and (len(second) == 1 or (len(second) > 1 and second[0] != '0')):
                        if proceed(num, first, second):
                            return True
        return False