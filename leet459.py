459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

用了KMP方法里面的前后缀相同的长度的next数组。如果是重复substring的话，这个next数组尾数为全长减去一个重复单元

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def get_next(s):
            next = [-1]
            k, j = -1, 0
            while j < len(s):
                if k == -1 or s[k] == s[j]:
                    k += 1
                    j += 1
                    next.append(k)
                else:
                    k = next[k]
            return next
        next_table = get_next(s)
        if next_table[-1] and len(s) % (len(s) - next_table[-1]) == 0:
            return True
        else:
            return False


第一个字母一定是substring第一个，最后一个一定是substring最后一个
s + s 刨了最后一个和第一个，破坏了前后两个，如果有重复单元的话，那么中间剩余的足够重复单元的
问题是这个为啥这么快，比前一个构建next的快得多，那个是线性的，这个要匹配，也需要最少kmp把，也是线性的
但是速度快了好多，肯能这个里面是C实现的吧。

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s*2)[1:-1]