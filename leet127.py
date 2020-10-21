127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def isNeighbour(node, word):
            diff, n = 0, len(word)
            for i in range(n):
                if node[i] != word[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        dic = {}
        for i in wordList:
            dic[i] = dic.get(i, 0) + 1
        que = [beginWord]
        level, count = {beginWord: 0}, 1
        while que:
            nextL = []
            for node in que:
                if node == endWord:
                    return level[node] + 1
                for idx in range(len(node)):
                    for replace in 'abcdefghijklmnopqrstuvwxyz':
                        if node[:idx] + replace + node[idx+1:] in dic:
                            nextL.append(node[:idx] + replace + node[idx+1:])
                            del dic[node[:idx] + replace + node[idx+1:]]
                            level[node[:idx] + replace + node[idx+1:]] = count
            que = nextL[:]
            count += 1
        return 0