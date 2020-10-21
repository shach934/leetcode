117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
    
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        currL, nextL = [], []
        if root : currL.append(root)
        while currL:
            last = currL[0]
            if currL[0].left: nextL.append(currL[0].left) 
            if currL[0].right: nextL.append(currL[0].right) 
            for i in range(1,len(currL)):
                if currL[i].left: nextL.append(currL[i].left) 
                if currL[i].right: nextL.append(currL[i].right) 
                last.next = currL[i]
                last = last.next
            last.next = None
            currL = nextL[:]
            nextL = []