84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

divide and conquer method. accepted but super slow. almost is beated by all. 


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # divide and conquer
        if len(heights) is 0:
            return 0
        maxL = self.rectangle(heights, 0, len(heights)-1)
        return maxL
    def rectangle(self, heights, left, right):
        if left == right:
            return heights[left]
        else:
            mid = left + (right-left)//2
            maxL = self.rectangle(heights, left, mid)
            maxR = self.rectangle(heights, mid+1, right)
            maxM = self.cross(heights, left, right)
        return max([maxL, maxR, maxM])
    def cross(self, heights, left, right):
        mid = left + (right-left)//2
        maxA, width, l, r, shortest = heights[mid], 1, mid, mid, heights[mid]
        while l > left or r < right:
            if l == left: 
                r += 1
                width += 1
                shortest = min(shortest, heights[r])
                maxA = max(maxA, shortest*width )
            elif r == right:
                l -= 1
                width += 1
                shortest = min(shortest, heights[l])
                maxA = max(maxA, shortest*width)
            else:
                if heights[l-1] > heights[r+1]:
                    l -= 1
                    width += 1
                    shortest = min(shortest, heights[l])
                    maxA = max(maxA, shortest*width)
                else:
                    r += 1
                    width += 1
                    shortest = min(shortest, heights[r])
                    maxA = max(maxA, shortest*width)
        return maxA
        
这个方法的关键点在于，每个colum能够组成的最大面积为： 以这个colum为最小值的所有的colume组合。比如说，heights里面最小的那个colume能够组成的最大的面积为全部的宽度乘以最小的colume的高度。所以，每个colum，向左和向右看，找到以这个左边和右边都比该colume大的所有colume，算出宽度乘以这个colume的高度即可。然后遍历所有的colum，找到最大的那个返回

但是以每个colum为最小值的范围不好找，可能需要On^2

用一个stack的做法就是，保证每次一个出栈的时候，当前的位置是右边边界，stack内的最后一个是左边边界。这样就能算出以出栈元素为最小值的左右边界。
每次遍历到一个colum，去跟stack最后一个进行比较，如果比当前的栈内边界元素小，那么说明当前的栈内最后一个元素已经找到了右边界，（因为当前比他小，以她为最小的不能越过右边了）
然后就出栈这个元素，根据当前的右边界和栈内最后一个元素决定的左边界，算出来面积。

这个code的巧妙之处在于添加了尾部一个0，然后stack内添加了一个 -1， python最后个元素刚好是-1.

class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, maxA = [-1], 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                r = stack.pop()
                w = i - stack[-1] - 1
                h = heights[r]
                maxA = max(maxA, h*w)
            stack.append(i)
        heights.pop()
        return maxA