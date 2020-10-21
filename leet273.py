273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """ 
        dicts = {0:'Zero',1:'One', 2:'Two', 3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
                11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',
                30:'Thirty', 40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'One Hundred',1000:'One Thousand', 1000000:'One Million',1000000000:'One Billion'}
        def hundreds(num):
            # transfer the hundreds number to english
            if num in dicts:
                return dicts[num]
            ans = ''
            if num > 100:
                hundDigi = num//100
                ans += dicts[hundDigi] + ' ' + 'Hundred'
                num %= 100
            if num == 0:
                return ans
            elif num <= 20:
                return ans + ' ' + dicts[num]
            else:
                deciDigi = num // 10
                ans += ' ' + dicts[deciDigi*10] 
                num %= 10
                if num:
                    ans += ' ' + dicts[num]
                if ans[0] is ' ':
                    return ans[1:]
                elif ans[-1] is ' ':
                    return ans[:-1]
                return ans
        if num in dicts:
            return dicts[num]
        unit = ['Thousand', 'Million', 'Billion']
        idx = -1
        ans = ''
        
        while num:
            cut = num % 1000
            if cut:
                hund = hundreds(cut)
                if idx >= 0 : 
                    ans = hund +  ' ' + unit[idx] + ' ' + ans
                else:
                    ans += hund
                num //= 1000
                idx += 1
            else:
                num //= 1000
                idx += 1
        if ans[0] is ' ':
            return ans[1:]
        elif ans[-1] is ' ':
            return ans[:-1]
        return ans