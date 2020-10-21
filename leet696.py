696. Count Binary Substrings

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.

自己写的解法，统计上一次出现同样数目的1和0的位置，然后去检查这之间是否0和1是连续的，如果不连续跳出
但是超时了，

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, count, static = 0, 0, {0:[-1]}
        for i in range(len(s)):
            if s[i] == '0':
                count -= 1
            else:
                count += 1
            if count in static:
                check = static[count]
                check = check[::-1]
                for j in check:
                    if self.valid(s[j+1:i+1]):
                        ret += 1
                    else:
                        break
                static[count].append(i)
            else:
                static[count] = [i]
            #print(static)
        return ret
    def valid(self, string):
        count = 0
        for i in range(1,len(string)):
            if string[i] != string[i-1]:
                count += 1
                if count == 2:
                    return False
        return True
        
discuss里面看到的解法，充分利用了0和1必须连续的条件 只需要统计相邻的0和1的最短长度然后加起来就可以了。
跟解数学题一个思路，条件要充分利用，拿来简化题目

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, count, static = 0, 1, []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
               static.append(count)
               count = 1
        static.append(count)
        
        for i in range(1, len(static)):
            ret += min(static[i-1], static[i])
        
        return ret