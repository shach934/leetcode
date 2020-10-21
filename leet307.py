307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


class SegTree(object):
    def __init__(self, left, right):
        self.range = [left, right]
        self.left = None
        self.right = None
        self.sum = 0
        self.val = 0

class NumArray(object):
    def build(self, left, right):
        if left == right:
            return SegTree(left,left)
        Node = SegTree(left, right)
        Node.right = self.build(left + (right-left)//2 + 1, right)
        Node.left = self.build(left, left + (right-left)//2)
        return Node
    
    def TreeUpdate(self, root, num, idx, old):
        it, diff = root, num - old
        while it:
            left, right = it.range[0], it.range[1]
            if left == right and left == idx:
                it.val = num
                it.sum = num
                return 
            if idx >= left and idx <= left+(right-left)//2 :
                it.sum += diff
                it = it.left
            elif idx > left+(right-left)//2 and idx <= right:
                it.sum += diff
                it = it.right
                
    def check(self, root, left, right):
        l, r = root.range[0], root.range[1]
        if l == left and r == right:
            return root.sum
        mid = l + (r - l) // 2
        if left >= l and right <= r :
            if mid >= left and mid < right:
                return self.check(root.left, left, mid) + self.check(root.right, mid+1, right)
            elif right <= mid:
                return self.check(root.left,left, right)
            elif left >= mid +1:
                return self.check(root.right, left, right)
    
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) > 0:
            self.root = self.build(0, len(nums)-1)
            for i in range(len(nums)):
                self.TreeUpdate(self.root, nums[i], i, 0)
            self.nums = nums[:]
        else:
            self.nums = []

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.TreeUpdate(self.root, val, i, self.nums[i])
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.check(self.root, i, j)