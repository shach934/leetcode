382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这道题是和398一样的，在一个很大的数据池中，随机选取一个出来，或者随机选取一组出来。
# 不确定池子的大小情况下。
# 算法叫 蓄水池算法。
# 从A池中，要选出来一组数字。那就先选前k个，然后从第j=k+1开始，随机去判定是否取该值。概率是p= k/j
# 比如 randint(1, j) == j。

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        itor, count =self.head, 0
        ans = 0
        while itor:
            count += 1
            if count == random.randint(1, count):
                ans = itor.val
            itor = itor.next
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()