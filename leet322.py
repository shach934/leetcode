322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for i in range(1, len(dp)):
            mini = 2**32
            for coin in coins:
                if coin <= i and dp[i-coin]:
                    mini = min(mini, dp[i-coin] + 1)
                elif i == coin:
                    mini = 1
                    break
            if mini < 2**32:
                dp[i] = mini
            else:
                dp[i] = 0
        if dp[-1]:
            return dp[-1]
        else:
            return -1