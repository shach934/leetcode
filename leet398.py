398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


# 这个解法的巧妙之处就是 根本不保留任何数组，只用一个变量count，然后从1到count之间选择，如果等于count的话，那就返回，否则就接着进行下去
# randint(1, count) 选到count的概率也是随机的。但是怎么保证一定会选上呢？
# 因为如果一旦这个target出现过，那么第一次randint（1，1）一定保证选上1，res保存到i，然后后面随机选到，但是如果不存在，那就返回None。这个后面的概率可能会比较小，第一个的概率会比较大吧。

class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res


# 这他妈都能过！竟然不会TLE，这个破题就完全是不让用任何多余的内存，但是可以花很多时间，毕竟测试用例的长度只有5。。。。无奈了。
class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])