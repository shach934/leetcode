# 66. Plus One

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        flag = True
        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                flag = False
                break
        if flag:
            digits += [1]
        return digits[::-1]