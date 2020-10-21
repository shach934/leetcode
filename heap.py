def heap_sort(nums):
    if len(nums) <= 1:
        return nums
    end = len(nums) - 1
    heapify(nums, end) 
    while end >= 0:
        nums[0], nums[end] = nums[end], nums[0]
        end -= 1
        siftDown(nums, 0, end)
    
    
def heapify(nums, end):
    start = len(nums) // 2
    while start >= 0:
        siftDown(nums, start, end)
        start -= 1
        
def shiftDown(nums, start, end):
    swap = start
    while swap*2+1 <= end:
        Lchild = start * 2 + 1
        if nums[Lchild] > nums[swap]:
            swap = Lchild
        if Lchild + 1 <= end and nums[Lchild + 1] > nums[swap]:
            swap = Lchild + 1
        if swap == start:
            return 
        else:
            nums[swap], nums[start] = nums[start], nums[swap]
            start = swap
nums = [2,31,546,4,3,4,6,7,8,9,34,6,5,4,3,3,5,4,1,2,5,8,8, 9]
heap_sort(nums)
print(nums)