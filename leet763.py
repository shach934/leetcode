763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dictory = {}
        for idx, letter in enumerate(S):
            if letter not in dictory:
                dictory[letter] = [idx]
            else:
                dictory[letter].append(idx)
        ans = []
        start, left, right, reach = 0, 0, 0, 0
        while right < len(S):
            finished = True
            for idx in range(left, right+1):
                if dictory[S[idx]][-1] > reach:
                    reach = dictory[S[idx]][-1]
                    finished = False
            if finished:
                ans.append([start, reach])
                start, left, right, reach = reach + 1, reach + 1, reach + 1, reach + 1
            else:
                left, right = right, reach
        
        return [item[1] - item[0] + 1 for item in ans]