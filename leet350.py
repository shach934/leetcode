# 350. Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# 1 What if the given array is already sorted? How would you optimize your algorithm?
# 2 What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 3 What if elements of nums2 are stored on disk, and the memory is limited such that 
  # you cannot load all elements into the memory at once?
  
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1, dict2, ret = {}, {}, []
        for i in nums1:
            dict1[i] = dict1[i] + 1 if i in dict1 else 1
        for i in nums2:
            dict2[i] = dict2[i] + 1 if i in dict2 else 1
        for keys in dict1:
            if keys in dict2:
                for idx in range(min(dict1[keys], dict2[keys])):
                    ret.append(keys)
        return ret