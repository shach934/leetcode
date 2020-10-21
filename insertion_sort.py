# insertion sort
def insertion_sort(nums, reverse = False):
    if reverse is False:
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1
            while i>=0 and nums[i] > key:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = key
    else:
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1
            while i>=0 and nums[i] < key:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = key
nums = [ 5, 5, 2, 4, 6, 1, 3]
insertion_sort(nums)
print(nums)