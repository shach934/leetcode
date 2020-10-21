3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
"pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        deq, dic, maxL = collections.deque(), {}, 1
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                deq.append(i)
                maxL = max(maxL, deq[-1] - deq[0] + 1)
            else:
                idx = dic[s[i]]
                while 1:
                    out = deq.popleft()
                    del dic[s[out]]
                    if out == idx:
                        break
                dic[s[i]] = i
                deq.append(i)
        maxL = max(maxL, deq[-1] - deq[0] + 1)
        return maxL 