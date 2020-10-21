# 93. Restore IP Addresses

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        solu = []
        self.dfs(s, solu, '', 0, 0)
        return solu
        
    def dfs(self, s, solu, curr, begin, count):
        if count == 3:
            if self.vaildIp(s[begin:]):
                curr +=  s[begin:]
                solu.append(curr)
        for i in range(begin+1, begin+4):
            if self.vaildIp(s[begin:i]):
                curr +=  s[begin:i] + '.'
                count += 1
                self.dfs(s, solu, curr, i, count)
                count -= 1
                curr = curr[0:len(curr)-(i-begin+1)]

    def vaildIp(self, s):
        if len(s) == 1 or (len(s) > 1 and s[0] != '0' and int(s) <= 255):
            return True 
        return False
dfs = Solution()
a = dfs.restoreIpAddresses('10024835') 
print(a)