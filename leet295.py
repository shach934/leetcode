295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.val) == 0:
            self.val.append(num)
        else:
            l, r = 0, len(self.val) - 1
            while l<r:
                mid = (l+r)//2
                if self.val[mid] == num:
                    l = mid
                    r = mid
                elif self.val[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            if self.val[l] == num:
                self.val.insert(l,num)
            elif self.val[l] > num:
                self.val.insert(l, num)
            else:
                self.val.insert(l+1,num)
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.val) % 2 == 0:
            return (self.val[len(self.val) // 2] +self.val[len(self.val) // 2 - 1]) / 2.0
        else:
            return self.val[len(self.val) // 2]*1.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()