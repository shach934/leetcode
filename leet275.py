275. H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        l, r = 0, len(citations) - 1
        while l <= r:
            mid = (l+r)//2
            if citations[mid] < len(citations) - mid:
                l = mid + 1
            else:
                r = mid - 1
        return len(citations) - 1 - r