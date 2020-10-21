264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 
1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums, record, i, curr = [1], {}, 1, 0
        while i<4*n:
            if 2*nums[curr] not in record:
                nums.append(2*nums[curr])
                record[2*nums[curr]] = 1
                i += 1
            if 3*nums[curr] not in record:
                nums.append(3*nums[curr])
                i += 1
                record[3*nums[curr]] = 1
            if 5*nums[curr] not in record:
                nums.append(5*nums[curr])
                record[5*nums[curr]] = 1
                i += 1
            curr += 1
        nums.sort()
        return nums[n-1]