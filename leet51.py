# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
 # [".Q..",  // Solution 1
  # "...Q",
  # "Q...",
  # "..Q."],

 # ["..Q.",  // Solution 2
  # "Q...",
  # "...Q",
  # ".Q.."]
# ]

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solut = []
        self.put(solut, [], n, 0)
        
        return solut
        
    def put(self, solut, nums, n, row):
        if row == n:
            tu = self.printQ(nums)
            solut.append(tu[:])
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
    def printQ(self, solut):
        ret =  []
        for i in range(len(solut)):
            row = ''
            for j in range(len(solut)):
                if solut[i] == j:
                    row += 'Q'
                else:
                    row += '.'
            ret.append(row)
        return ret