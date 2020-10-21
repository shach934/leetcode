215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.heapify(nums, k-1)
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[i], nums[0] = nums[0], nums[i]
                self.siftDown(nums, 0, k-1)
        return nums[0]
        
        heapify(self, nums, end):
            start = end//2
            while start >= 0:
                self.siftDown(nums, start, end)
                start -= 1
        
        siftDown(self, nums, start, end):
            swap = start:
            while start*2+1<=end:
                Lchild = start*2+1
                if nums[Lchild] < nums[start]:
                    swap = Lchild
                if Lchild + 1 <= end and nums[Lchild+1] < nums[swap]:
                    swap = Lchild + 1
                if swap == start:
                    return 
                nums[swap], nums[start] = nums[start], nums[swap]
                start = swap