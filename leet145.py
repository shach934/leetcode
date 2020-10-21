# 145. Binary Tree Postorder Traversal

# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
   # 1
    # \
     # 2
    # /
   # 3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.houxu(root, ret)
        return ret
    def houxu(self, root, ret):
        if root:
            self.houxu(root.left,ret)
            self.houxu(root.right,ret)
            ret.append(root.val)

# 非递归版本，
# 需要一个标记，标记当前的根节点访问过与否, 首次遇到的时候 压栈 同时添加一个0到mark里面去
# 弹栈的时候去看一下mark，是否为1，如果不为1说明为首次访问，右子树还未方位，挪到右之树去，同时把mark改成1 下次遇到弹栈

        ret,mystack, mark = [], [], []
        while root or len(mystack):
            while root:
                mystack.append(root)
                mark.append(0)
                root = root.left
            if mark[-1]:
                ret.append(mystack[-1].val)
                mark.pop()
                mystack.pop()                
            else:
                root = mystack[-1].right
                mark[-1] = 1   
        return ret