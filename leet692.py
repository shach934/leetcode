692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        mydict = {}
        for i in words:
            mydict[i] = mydict.get(i, 0) + 1
        mylist = list(mydict.items())
        bucket = [[] for i in range(len(words))]
        for i in mylist:
            bucket[i[1]].append(i[0])
        for i in range(len(bucket)):
            if len(bucket[i]):
                bucket[i].sort()
        ret, idx = [], len(bucket) - 1
        while len(ret) <= k:
            if len(bucket[idx]):
                ret += bucket[idx]
            idx -= 1
        return ret[:k]