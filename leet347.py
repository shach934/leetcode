# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

先用一个hash table统计出来每个元素的频率
然后按照频率排序，给出前k个元素，这样的复杂度是O(n log n), 

更快的两个方法
1 按照快排的方式来，选择一个pivet，然后把比他大的放在他的后面，比他小的放在他的前面，最终他就被放在了自己应该的位置
如果位置为k，那么返回所有他前面的元素，否则看偏后还是偏前面，去对应的子序列里面找。复杂度是 O（n log k）。如果用改进的
第K大的数字方法，每5个数字一组，排序，取中位数，然后中位数的中位数，作为pivet，然后重复这个过程，可以做到线性。O（n）

2 按照堆的方法来做，维持一个K的最小堆，每次把一个元素放到这个最小堆里面，如果比堆顶小，放到堆顶，更新最小堆。复杂度是
O（nlogk）， 会比优化的方法1慢，但是好处是这个把数组扫描一遍就结束了，n，logk来每次更新堆，如果数据量巨大，访问不便，好！

唉。。。其实就是两个经典的排序方法：快排和堆排的两个变种 
绕不过去，还是把这俩实现一遍吧。畏难是不行的   @@！

最快的一种办法，空间换时间，桶排序。本题中的频率是有明确上下限的，频率最大值也就是数组长度，并且都还是整数，最适合用桶排序的
估计leetcode的测试样例的长度太小，bucketsort并没有体现出速度优势，和heapsort的速度基本一致，如果n和k都很大的话，桶排序可能会更快吧
因为最多也就是两遍遍历就完了。3n就能解决战斗

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap implementation
        # heapify the first k element to form a minimum heap. then compare the 
        # rest elements with the heap top, if larger, replace heap top with it. 
        mydict, ret= {}, []
        bucket = [[] for i in range(len(nums))]
        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        nums = list(mydict.items())

        for i in range(len(nums)):
            bucket[nums[i][1]-1].append(nums[i][0])
        idx = len(bucket) - 1
        while len(ret)<=k-1:
            if len(bucket[idx]):
                ret += bucket[idx]
            idx -= 1
        return ret
        
        
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap implementation
        # heapify the first k element to form a minimum heap. then compare the 
        # rest elements with the heap top, if larger, replace heap top with it. 
        mydict= {}
        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        nums = list(mydict.items())
        self.heapify(nums, k-1)
        for i in range(k, len(nums)):
            if nums[i][1] > nums[0][1]:
                nums[i], nums[0] = nums[0], nums[i]
                self.siftDown(nums, 0, k-1)
        return [nums[i][0] for i in range(0,k)]
        
    def heapify(self, nums, k):
        start = k // 2
        while start >=0:
            self.siftDown(nums, start, k)
            start -= 1
            
    def siftDown(self,nums, start, end):
        swap = start
        while start * 2 + 1 <= end:
            Lchild = start*2+1
            if nums[Lchild][1] < nums[swap][1]:
                swap = Lchild 
            if  Lchild + 1 <= end and nums[Lchild + 1][1] < nums[swap][1]:
                swap = Lchild + 1
            if swap == start:
                return 
            nums[swap], nums[start] = nums[start], nums[swap]
            start = swap
            
# 基于快排的思想不奏效啊。。。。快排本身会写了，但是这个修改版的怎么都不work。回头再弄一次吧。
# 这个题最好的应该是用bucketsort，桶排序，因为保证了范围，最多就是一模一样的元素，频率是num的长度 O（n）复杂度，就是比较耗费空间而已
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heap implementation
        # heapify the first k element to form a minimum heap. then compare the 
        # rest elements with the heap top, if larger, replace heap top with it. 
        mydict= {}
        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        nums = list(mydict.items())
        start, end = 0, len(nums) - 1
        while 1:
            p = self.partition(nums,  start, end)
            if p == k - 1:
                return [nums[i][0] for i in range(0, k)]
            else:
                if p > k-1:
                    end = p
                else:
                    start = p
                    
    def partition(self,nums, start, end):
        pivot = nums[-1]
        i, j = start - 1, end + 1
        while 1:
            while 1:
                i += 1
                if nums[i][1] >= pivot[1]:
                    break
            while 1:
                j -= 1
                if nums[j][1] <= pivot[1]:
                    break
            if i >= j:
                return j
            else:
                nums[i] , nums[j] = nums[j] , nums[i]