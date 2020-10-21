390. Elimination Game

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, tail, length, step, forward = 0, n-1, n, 2, True
        while length > 1:
            if forward:
                head = head + step // 2
                #print([i+1 for i in range(head, n, step)])
                length //= 2
                tail = head + step * (length - 1)
                step *= 2
                forward = False
            else:
                tail = tail - step//2
                length //= 2
                head = tail - step * (length - 1)
                #print([i for i in range(head, tail+1, step)])
                step *= 2
                forward = True
        return head + 1 