394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, 
k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

其实就是自己实现了一个递归栈，因为这个递归也不好处理，所以这个递归栈反而是很简洁的。效率也高

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        Stack = [[1, '']]
        num = ''
        for i in s:
            if i.isalpha():
                Stack[-1][1] += i
            if i.isdigit():
                num += i
            if i is '[':
                Stack.append([int(num), ''])
                num = ''
            if i is ']':
                times, string = Stack.pop()
                Stack[-1][1] += times*string
        return Stack[0][1]
        
        
obj = Solution()
a = obj.decodeString('"3[a]2[ba2[c]f]edf"')
print(a)