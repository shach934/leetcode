223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right 
corner as shown in the figure.

Assume that the total area is never beyond the maximum possible value of int.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if C <=  E or G <= A or D <= F or H <= B:
            return (D-B)*(C-A) + (H-F)*(G-E)
        else:
            if A > E:
                if C>G:
                    x = G - A
                else:
                    x = C- A
            else:
                if C> G:
                    x = G - E
                else:
                    x = C - E

            if B >  F:
                if H <  D:
                    y = H - B
                else:
                    y = D - B
            else:
                if H <  D:
                    y = H - F
                else:
                    y = D - F
        return (D-B)*(C-A) + (H-F)*(G-E) - x * y