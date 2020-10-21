423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

顺序是关键，一定找到合适的顺序，主要是独特的字母

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = ['eight','zero','six','two', 'four','seven', 'five', 'three','nine', 'one']
        squen = [8,0,6,2,4,7,5,3,9,1]
        aim, nums = {}, {}
        for i in s:
            aim[i] = aim.get(i,0)+1
        while aim:
            for i in range(10):
                exist = True
                many = 2**32
                for j in words[i]:
                    if j not in aim:
                        exist = False
                    else:
                        many = min(many, aim[j])
                if exist:
                    for j in words[i]:
                        aim[j] -= many
                        if aim[j] == 0:
                            del aim[j]
                    nums[squen[i]] = nums.get(squen[i], 0) + many
        ret = ''
        for i in range(10):
            ret += str(i) * nums.get(i, 0)
        return ret