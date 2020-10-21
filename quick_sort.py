# quick_sort

# Lomuto partition version

初始化i = - 1，j从lo 到hi
然后挨个与pivot比较，如果比pivot大就不动
如果比pivot小的话，那么交换i和j，然后j加一
只有比pivot小的时候 i才会往前走，就是说， i记录的是比pivot小的数的最后一个
然后从j里面发现一个更小的，那么就i往前走一步，找到一个大的，交换后面发现的小的
这样保证小的在前面，也保证了i仍然指向最后一个小的。
精妙啊！但是据说效率不好，

def quick_sort(nums, lo, hi):
    if lo < hi:
        x = partition(nums, lo, hi)
        quick_sort(nums, lo, x-1)
        quick_sort(nums, x+1, hi)
        
def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo - 1
    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    if nums[hi] < nums[i+1]:
        nums[i+1], nums[hi] = nums[hi], nums[i+1]
    return i + 1
nums = [20,31,3,42,566,32,5]
quick_sort(nums, 0, len(nums) - 1)
print(nums)



def quick_sort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        quick_sort(nums, lo, p)
        quick_sort(nums, p+1, hi)
def partition(nums, lo, hi):
    pivot = nums[lo]
    i = lo - 1
    j = hi + 1
    while 1:
        # 不能用while代替原来的，因为原来的保证每次最少i都会往前走一步
        # 如果相同的存在，那么也会走过去的
        # 用while和if实现do while，这个时候要注意，条件是相反的，dowhile是满足
        #条件时候继续，while1 if是在不满足条件时跳出。这个跳出的条件一定是要与
        #do while是互补的！！！这样才能处理相同元素的问题
        while 1:
            i += 1
            if nums[i] >= pivot:
                break
        while 1:
            j -= 1
            if nums[j] <= pivot:
                break
        if i>=j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
        
nums = [20,31,3,42,566,32,5]
quick_sort(nums, 0, len(nums) - 1)
print(nums)