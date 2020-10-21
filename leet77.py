77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

# 递归的进行排列组合 很容易就超时了。

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        if k == 0:
            return [[]]
        for i in range(1, n+1):
            self.helper(n, k, [i], ret)
        return ret

    def helper(self, n, k, curr, ret):
        if len(curr) == k:
            return ret.append(curr[:])
        for i in range(curr[-1]+1, n+1):
            curr.append(i)
            self.helper(n, k, curr, ret)
            curr.pop()
            
            
            
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ret;
        vector<int> curr;
        for(int i= 1; i<=n; i++){
            curr.push_back(i);
            helper(n, k, curr, ret);  
            curr.pop_back();
        }
        return ret;
    }
    
    void helper(int n, int k, vector<int> &curr, vector<vector<int>> & ret){
        if(curr.size() == k)
            ret.push_back(curr);
        for(int i= curr[curr.size() - 1]+1; i <=n; i++){
            curr.push_back(i);
            helper(n, k, curr,  ret);
            curr.pop_back();
        }
    }
};