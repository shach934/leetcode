670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum 
valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numbers = [[int(i)] for i in str(num)]
        for i in range(len(numbers)):
            numbers[i].append(i)
        seq = sorted(numbers, cmp = lambda x, y: (x[0] -y[0]) or (y[1] - x[1]), reverse = True)
        for i in range(len(numbers)):
            if numbers[i][0] < seq[i][0]:
                idx = i
                while idx + 1 < len(numbers) and seq[i][0] == seq[idx+1][0]:
                    idx += 1
                idx = seq[idx][1]
                numbers[i], numbers[idx] = numbers[idx], numbers[i]
                break
        return int(''.join([str(numbers[i][0]) for i in range(len(numbers))]))