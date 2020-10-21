113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
    
class Solution(object):
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ret = []
        self.helper(root, summ, [], ret)
        return ret
 
    def helper(self, root, summ, route, ret):
        if root is not None:
        这里面有一个非常tricky的地方，就是不能直接把新的root value append到route里面去，
        因为route只会有一份！！不论是哪个递归函数修改了，都会被改掉的，所以
            a = route + [root.val]
            if root.left is None and root.right is None and sum(a)== summ:
                ret.append(a)
            else:
        这里不能把值加入到route里面然后传参数进去，那么就不会创建新的进程和列表了，目前这种方式每次都会创建一个新的list，赋给递归的route！！！python的一个特性吧
                self.helper(root.left, summ, route + [root.val], ret)
                self.helper(root.right, summ, route + [root.val], ret)