"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

非常麻烦的先找出来所有的peak，然后这些peak在往里面灌水的时候，有些peak不能构成dam，会被淹了。第二轮把淹了的踢出去。
然后再挨个统计水的体积出来的。

难的在第二步，怎么才能找到那些会被淹了的peak。关键在于记住左边的dam，然后一直往右走，看到一个如果peak放进去，然后遇到下一个peak的时候，看看是不是比
栈里面放的那个peak要高，并且那个放进去的peak也比左边的大坝低，说明新的这个peak能够和左边的大坝构成一个更高的水库把栈里面的这个peak淹了。就把他踢出去

整体还是线性的
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        height.append(0)
        peak, n, V =  [], len(height), 0
        if height[0] > height[1]:
            peak.append(0)
        for i in range(1,len(height)-1):
            if height[i] >= height[i-1] and height[i] >= height[i+1]:
                if not (height[i] == height[i-1] and height[i] == height[i+1]):
                    peak.append(i)
        if height[n-1] > height[n-2]:
            peak.append(n-1)
        stack, level = [peak[0]], height[peak[0]]
        for i in range(1,len(peak)):
            while len(stack) > 1 and height[stack[-1]] < level and height[stack[-1]] < height[peak[i]] :
                stack.pop()
            stack.append(peak[i])
            level = max(level, height[peak[i]])

        for i in range(len(stack)-1):
            level = min(height[stack[i]], height[stack[i+1]])
            for col in range(stack[i], stack[i+1]+1):
                V += max(0, level - height[col])
        return V