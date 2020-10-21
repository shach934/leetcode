12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        opts =   [1000,  500, 100,  50,  10,   5,   1]
        roman = ['M',     'D',   'C',   'L',   'X',  'V',  'I']
        
        """
        4     and 9, 
        40   and 90
        400 and 900 
        need to use subtract rule instead of summation rule.
        """
        
        ans = ''
        if num >= 1000:
            ans += num//1000 * 'M'
            num -= (num//1000) * 1000 
        idx = 1
        for idx in range(1, len(opts)-1, 2):
            if num > opts[idx+1]:
                if num > opts[idx]:
                    if num//opts[idx+1] == 9:
                        ans += roman[idx+1] + roman[idx-1]
                    else:
                        ans += roman[idx] + roman[idx+1]*(num//opts[idx+1] - 5)
                        
                    num -= (num//opts[idx+1])*opts[idx+1]
                elif num < opts[idx]:
                    if num//opts[idx+1] == 4:
                        ans += roman[idx+1] + roman[idx]
                    else:
                        ans += roman[idx+1] * (num // opts[idx+1])
                    num -= (num//opts[idx+1]) * opts[idx+1]
                else:
                    ans += roman[idx]
                    num -= opts[idx]
            elif num == opts[idx+1]:
                ans += roman[idx+1]
                num -= opts[idx+1]
        return ans