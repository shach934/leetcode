168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        letters = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        while n:
            cut = n%26
            ret = letters[cut] + ret
            if cut == 0:
                n = n//26 - 1
            else:
                n = n // 26
        return ret