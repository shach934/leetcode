#coding=utf-8

# leetcode 756
# depth first search. construct the above level blocks in each turn
# 只是要找到是否可以，而不需要最短路径，或者所有的结果，那就深搜，找到立刻返回。

# 但是每次进行递归的时候，只要有一个字母填上了就要往下递归了，不能是一行一行的递归。
# 要不就是两层递归，行内一层，行行一层。那样就太麻烦了。

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        
        def dfs(row, nextRow, idx, allowed):
            if len(nextRow) == len(row) - 1:
                row = nextRow
                nextRow = ''
                idx = 0
            if len(row) == 1:
                return True
            while idx < len(row) - 1:
                for term in allowed:
                    if row[idx:idx+2] == term[:2]:
                        nextRow += term[-1]
                        goDeep = dfs(row, nextRow, idx + 1, allowed)
                        if goDeep:
                            return True
                        else:
                            nextRow = nextRow[:-1]
                idx += 1
            return False
        nextRow = ''
        return dfs(bottom, nextRow, 0, allowed)