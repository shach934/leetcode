"""
52. N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solut = [0]
        self.put(solut, [], n, 0)
        return solut[0]
    def put(self, solut, nums, n, row):
        if row == n:
            solut[0] += 1
        for i in range(n):
            if self.ifPut(nums, i):
                nums.append(i)
                self.put(solut, nums, n, row+1)
                nums.pop()        
    def ifPut(self, nums, j):
        for i in range(len(nums)):
            if nums[i] == j or abs(i-len(nums)) == abs(nums[i] - j):
                return False
        return True