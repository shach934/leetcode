# leet506 Relative Ranks

# Given scores of N athletes, 
# find their relative ranks and the people with the top three highest scores, 
# who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, 
# so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their 
# relative ranks according to their scores.

# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		indx = 1
		mylist = []
		for p in nums:
			mylist.append([p, indx])
			indx += 1
		mylist.sort(key = lambda my:my[0], reverse = True)
		indx = 1
		for p in mylist:
			p.append(indx)
			indx += 1
		mylist.sort(key = lambda my:my[1])
		out = []
		for p in mylist:
			if p[2] == 1:
				out.append("Gold Medal")
			elif p[2] == 2:
				out.append("Silver Medal")
			elif p[2] == 3:
				out.append("Bronze Medal")
			else:
				out.append(str(p[2]))
		return out