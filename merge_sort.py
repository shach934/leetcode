#merge sort
def merge_sort(nums, p, q, r):
    if p<r:
        merge_sort(nums, p, q)
        merge_sort(nums, p+1, r)
        merge(nums, p, q, r)
        
def merge(nums, p, q, r):
    L, R = [], []
    for i in range(q-p+1):
        L.append(nums[i])
    for j in range(q, r+1):
        R.append(nums[j])
    L.append(float('inf'))
    R.append(float('inf'))
    i, j = 0, 0
    