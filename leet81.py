81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bSearch(nums, l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return True
            return False
        
        def helper(nums, l, r, target):
            if l == r:
                return nums[l] == target
            elif l > r:
                return False
            # 数组是正序的，没有经过旋转，直接用二分查找就可以了
            if nums[l] < nums[r]:
                return bSearch(nums, l, r, target)
            # 数组经过旋转了
            while l < r:
                mid = (l + r) // 2
                # 无法判断是哪边，两边分开去找
                if nums[l] == nums[r] == nums[mid]:
                    return helper(nums, l, mid, target) or helper(nums, mid+1,r,target)
                # mid可能有两种情况，一个是在断点前，一个在后，分情况讨论
                elif target > nums[mid]:
                    # 如果mid比左边大，说明在断点前，此时只需要看右边的就可以了。相等的话无法判断
                    if nums[mid] > nums[l]:
                        l = mid + 1
                    # mid在断点之后，需要找出来target是在mid到结束，还是在断点前，相等无法判断
                    elif nums[mid] < nums[r]:
                        # 如果右边比target小，说明target在断点前
                        if nums[r] < target:
                            r = mid - 1
                        # 如果右边比target大，说明target在断点后。
                        elif nums[r] > target:
                            l = mid + 1
                        else:
                            return True
                    # 这时无法判断mid是在左边还是右边，分开查找拉倒
                    else:
                        return helper(nums, l, mid, target) or helper(nums, mid+1,r,target)
                # 跟前面一样，判断mid在断点前还是后面，分情况讨论
                elif target < nums[mid]:
                    # mid比左边大，说明在断点前
                    if nums[mid] > nums[l]:
                        # 说明target不可能在断点前，去后面找
                        if nums[l] > target:
                            l = mid + 1
                        # 说明targett在l和mid之间
                        elif nums[l] < target:
                            r = mid - 1
                        else:
                            return True
                    # mid比左边小，说明mid在断点后面，target一定只能在断点到mid之间了。
                    elif nums[mid] < nums[l]:
                        r = mid - 1
                    # 不管是mid可能与l或者r相同，都无法判断mid在左边还是右边。只能笨笨去搜了。
                    else:
                        return helper(nums, l, mid, target) or helper(nums, mid+1,r,target)
                else:
                    return True
            return nums[l] == target
                
        return helper(nums, 0, len(nums) -1, target)