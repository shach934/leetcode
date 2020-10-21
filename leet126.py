126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
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
        parent = {beginWord: []}
        done = False
        while que and not done:
            nextL = []
            for node in que:
                if node == endWord:
                    done = True
                for idx in range(len(node)):
                    for replace in 'abcdefghijklmnopqrstuvwxyz':
                        option = node[:idx] + replace + node[idx+1:]
                        if  option in dic and (option not in level or level[option] == count):
                            if option not in level:
                                nextL.append(option)
                                level[option] = count
                                parent[option] = [node]
                            elif option in level:
                                parent[option].append(node)
            que = nextL[:]
            count += 1
        if done:
            ret = [[endWord]]
            while ret[-1][-1] != beginWord:
                retNext = []
                for path in ret:
                    if (parent[path[-1]]) is 1: 
                        retNext.append(path+parent[path[-1]])
                    else:
                        for word in parent[path[-1]]:
                            retNext.append(path + [word])
                ret = retNext[:]
            for i in range(len(ret)):
                ret[i] = ret[i][::-1]
            return ret
        else:
            return []