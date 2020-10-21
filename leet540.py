# 540. Single Element in a Sorted Array

# Given a sorted array consisting of only integers where 
# every element appears twice except for one element which 
# appears once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        print(l,r)
        while l<r:
            mid = int((l+r)/2)
            if nums[mid + 1] == nums[mid]:
                if len(nums[:mid]) % 2:
                    r = mid - 1
                else:
                    l = mid + 2
            elif nums[mid - 1] == nums[mid]:
                if len(nums[:(mid - 1)]) % 2:
                    r = mid - 2
                else: 
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]

# 妈蛋的，list的slice，竟然是不包含后面的那个数字的！！！

# 其实就是去判断哪个是奇数哪个是偶数。决定是取前半截还是后半截
# 不管前后哪个相等，都能移动