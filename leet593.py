593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        #思路陷入了误区啊，并不一定刚好边与坐标轴平行
        dist, points = [], [p1,p2,p3,p4]
        for i in range(4):
            for j in range(i+1,4):
                temp = (points[i][0] - points[j][0])**2 + (points[i][1]-points[j][1])**2
                if temp != 0:
                    dist.append(temp)
        #print(dist)
        if len(dist) != 6:
            return False
        dist.sort()
        if dist[0] == dist[1] and dist[1] == dist[2] and dist[3] == dist[2] and dist[4] == dist[5]:
            return True
        else:
            return False