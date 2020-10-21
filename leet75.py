# 75. Sort Colors

# Given an array with n objects colored red, white or blue, sort them so that objects of 
# the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# click to show follow up.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, 
# then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# two passes beats 100.00% of python submissions 神马情况，为啥会这么快，实际上比大部分的one pass的都要快
        zeros, ones, twos = 0,0,0
        for i in range(len(nums)):
            if nums[i] is 0:
                zeros += 1
            elif nums[i] is 1:
                ones += 1
            else:
                twos += 1
         for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0 
            elif i >= zeros and i < zeros + ones:
                nums[i] = 1
            else:
                nums[i]  = 2     

                
# one pass solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros, twos = 0,0,len(nums)-1
        while nums[zeros] == 0:
            zeros += 1
            if zeros == len(nums):
                return 
        while nums[twos] == 2:
            twos -= 1
            if twos == 0:
                return 
        it = zeros + 1
        while it <= twos:
            if nums[it] == 0 and it > zeros:
                nums[it], nums[zeros] = nums[zeros], nums[it] 
                zeros += 1
            elif nums[it] == 2 and it < twos:
                nums[it], nums[twos] = nums[zeros], nums[twos] 
                twos -= 1
            elif nums[it] == 1:
                it += 1
                
                
one pass solution, 其实这个题目是快排的变种，pivot不再是一个数字，而是一组数字。
想法仍然和快排类似，挨个去看，如果小了，就扔到前面，如果大了就扔到后面，相等，pass
数字分为三组，bottom，middle，top
用but， mid， top分别记录bottom的上限，middle的上限，top的下限，这里面的标识都是过了一个的，即but左边完全为0， but本身不管， top右边全是2，top本身不管
but和top均为下一个待选位置

每个等待比较分组的数字为mid，如果他属于bottom，把他和bottom交换，0就进入了bottom，but加一，交换过来到mid的这个数字，有两种情况

第一种情况，but和mid相同，那么就说明mid也是指向0，换完了一样，就mid直接进入到下一个就好了。
第二种情况，but和mid不同，那么but到mid之间一定全是1，不可能是2，因为如果有2的话早就扔到后面去了，交换过来的数字mid不变，一直到mid指向的是1的时候才往后走。
所以but和mid之间一定全是1，那么这种情况下把0交换到bottom，把mid交换过来，这个位置不用比了，直接到下一个位置也不会出错。

如果mid属于top，把他和top交换，top减一 mid这个数字交换过来的，有可能属于别的，不一定是middle，所以mid不变 保证了but一定小于mid
当mid超过了top，那么mid就一定是2，不用再比了。退出

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        but, mid, top = 0, 0, len(nums) - 1
        while mid <= top:
            if nums[mid] == 0:
                nums[but], nums[mid] = nums[mid], nums[but]
                but, mid = but + 1, mid + 1
            elif nums[mid] == 2:
                nums[mid], nums[top] = nums[top], nums[mid]
                top -= 1
            else:
                mid += 1