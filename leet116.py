116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
层续遍历
    
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        currL, nextL = [], []
        if root: currL.append(root)
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