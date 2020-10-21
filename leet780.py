780. Reaching Points

这个题有点儿trick，节点从x,y出发到达x x+y和x+y， y。就是每个节点都能够有两个子节点。就构成了一个完全二叉树。这个二叉树每层下去的叶子节点就超级多了。
我最初用的广搜，广搜一层一层的往下，但是这个数量翻翻的下去 超级多节点，就没办法了，超时！

但是从叶节点往上走的话，就只有一条路了，不会有多余的分叉了，因为没有负位置，不管是x，y，只能是大的减小的，就只有一条路。
当tx>ty,就直接tx %= ty, 不用直接用减，如果减的话，可能要减去好多好多次可能，就会超时
tx可以直接用reminder，在reminder之前，tx 一定是一直大于ty的，所以直接用mod最好。

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx <= tx and sy <= ty:
            if (sx == tx and (ty - sy) % sx == 0) or (sy == ty and (tx - sx)%sy==0):
                return True
            if tx > ty :
                tx %= ty
            else:
                ty %= tx
        return False