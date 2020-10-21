"""6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

怎么写出bug free的code，这个题的主要注意点在，如果行的数目大于s的长度，
在添加每行的index的时候，需要考虑超出了s长的情况。
""" 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= 2 or numRows >= len(s):
            return s
        period = 2*numRows - 2
        ret = ''
        firstR = ''.join([s[i] for i in range(0, len(s), period)])
        ret += firstR
        for row in range(1,numRows-1):
            idxR = []
            for idx in range(row, len(s), period):
                idxR += [idx, idx + period - row * 2]
            while idxR[-1] >= len(s):
                idxR.pop()
            ret += ''.join([s[i] for i in idxR])
        lastR = ''.join([s[i] for i in range(numRows-1, len(s), period)])
        ret += lastR
        return ret