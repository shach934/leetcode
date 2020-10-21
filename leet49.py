"""
49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            stac = [0]*26
            for ell in s:
                stac[ord(ell) - ord('a')] += 1
            ss = ''.join([str(i) for i in stac])
            if ss in dic:
                dic[ss].append(s)
            else:
                dic[ss] = [s]
        ret = []
        for i in dic.items():
            ret.append(i[1])
        return ret
"""    
第一个版本类似于bucket sort， On的算法
第二个版本先排序，然后再放到dict里面去 O nlogn的算法
但是第二个比第一个快很多。
怀疑是由于单词的长度比26要短很多造成的。
"""

class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            ss = ''.join(sorted(s))
            dic[ss] = dic.get(ss,[]) + [s]
        return dic.values()