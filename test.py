from collections import Counter
import functools
import math
import random
import queue
import numpy as np


i = [i for i in range(5)]
j = [j for j in range(5)]
print(i)
print(j)
k = [m - n for m, n in zip(i, j)]

print(k)

x = [i for i in range(10)]
print(x * 10)
a = ((1,2,3), (4,5,0))

print(a)

s = "aab"
print(s[1::-1])

q1 = queue.Queue()
q2 = queue.Queue()
q1.put(1)
q1.put(2)
q2 = q1
print(q2.get())
print(q2.get())
a  = 'ABCD'
print(a.lower())
nums = [1,2,3]

dp = [[[0,0]] * 3 for i in range(3)]
print(dp)

random.shuffle(nums)
print(nums)

record = {}
record[(1,2)] = 1
print(record)

a = [True, True, True, True]
a[1:2:]=[False]*len(a[1:2:])
print(a)

print(10&1)

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print(all([ matrix[i][0] for i in range(4)]))

for i in range(10,-1, -1):
    print(i)

dic = {1:1}
dic[1] = 0
print(dic)

print(len(str(2**32)))
x = '2' + '0'*5
print(x.split('+'))

print(ord('b') - ord('a'))

a = [1,2]
a[0], a[1] = a[1], a[0]
print(a)
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(0)
b = []
b += [a] 


print(min(1,2))
a = [1,2]
a = [ a+[4]+a, a +[1]]
print(a)


def test():
    global  a
    a = 2
    print(a)
    return a
a=1
a = test()
print(a)

a = [[1,2]]
print(a[0])

a = ['5','8']
a[1] = '3'
print(a)
nums = [0, 1, 8, 12]
num = [nums[(i + 3)%4] for i in range(0,4)]
print(num)

print(max(nums))
nums += ['2' for i in range(10)]
print(nums)
print(list(filter(None, nums)))
zeros = [i for i in range(len(nums)) if nums[i] == 0]
nums = [nums[i] for i in range(len(nums)) if i not in zeros]
print(nums)
print(nums + [0 for i in range(2)])
print(functools.reduce(lambda x, y:x + y, range(3)))
print(float('inf'))
nums1 = [1, 2, 2, 1]
print([3+i for i in nums1])

print(len(nums1[:1]))
nums1.pop(0)
print(nums1)
print(set(range(10)))

for i in range(1):
    print(i)
nums1 = [1, 2, 2, 1]


nums2 = [2, 2]
print(sum([nums1,nums2], []))  # 这个是把整个list摊平了。

dict1,dict2 = {},{}
for i in nums1:
    dict1[i] = dict1[i] + 1 if i in dict1 else 1
for i in nums2:
    dict2[i] = dict2[i] + 1 if i in dict2 else 1
print(dict1, dict2)

print(len(dict1.keys()))

nums = [0,3,4,2]
if nums:
    print(nums + [43])

nums.extend([10,None])
print(nums)
num2 = [313]
nums = num2
del nums[:]
print(nums, num2)
findNums = [4,1,2]
print(findNums*2)
nums = [1,3,4,2]
dict1 = {}
l = len(nums)
lf = len(findNums)
ret = [-1]*lf
for i in range(l):
    dict1[nums[i]] = i
print(dict1)
for i in range(lf):
    for j in range(dict1[findNums[i]], l):
        if nums[j] > findNums[i]:
            ret[i] = nums[j]
            break
print(ret)


##############################################
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

nl, nc = 0, 0
row, col = len(grid), len(grid[0])
for r in range(row):
    for c in range(col):
        if grid[r][c] == 1:
            nl += 1
            if r + 1 <row and grid[r + 1][c]:
                nc += 1
            if c + 1 <col and grid[r][c + 1]:
                nc += 1
print(nl,nc)
print( 4*nl - 2*nc )

#############################################
a = [[1,2],[3,4]]
ret = []
for i in a:
    ret.extend(i)
print(ret)
###############################################
s = "cbaebabacb"
p = "abc"
ret = []
pdict = Counter(p)
subS = Counter(s[:(len(p))])
if(subS == pdict):
    ret.append(0)
for idx in range(len(p), len(s)):

    if s[idx] in subS:
        subS[s[idx]] += 1
    else:
        subS[s[idx]] = 1
    print(idx - len(p))
    print(s[idx - len(p)])
    subS[s[idx - len(p)]] -= 1
    if subS[s[idx - len(p)]] == 0:
        del subS[s[idx - len(p)]]
    if(subS == pdict):
        ret.append(idx - len(p) + 1)
print(ret) 
#############################################
s="abc" 
p= "bac"

s = Counter(s)
p = Counter(p)
print(s==p)
############################################
a = ["hello", "Alaska", "Dad", "Peace"]

row1 = set('qwertyuiop')
print(sorted(a[0]))
row2 = set('asdfghjklASDFGHJKL')
row3 = set('zxcvbnmZXCVBNM')
out = []
for i in a:
    w = set(i)
    if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
        out.append(i)
print(out)
#################################################################

print(set(a))
a = 'lets cray'
s = a.split(' ')
b = ''
for w in s:
    b = b + w[::-1] + ' '
print(b[:-1:])

a = "1+-1i" 
b = "1+-1i"
a1 = int(a.split('+')[0])
b1 = int(a.split('+')[1][:-1])

a2 = int(b.split('+')[0])
b2 = int(b.split('+')[1][:-1])
a = a1*a2 - b1 * b2
b = a2*b1 + b2*a1
print("%d+%di" %(a,b))

moves = "UDLRDD"
a = moves.count('L')
print(a)

nums = [3,2,1,6,0,5]
print(nums)
print(nums[:nums.index(max(nums))])
print(nums[nums.index(max(nums)) + 1:])


a = ~0b0
num = 5
while num & a:
    a = a<<1
    print(a)
print(~a & ~num)


b = bin(5)
print(b)
print(b.index('1'))

a = [1,2,3,4]
a.sort()
print(sum(a[0:-1:2]))

print(a)
s = "MCMXCVI"
for i in range(len(s)- 1): 
	print(i)
mydict = {'L':[-1, 0], 'R':[1, 0]}
from collections import Counter
roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
a = Counter(s)
sum = 0
for i in a:
	sum += a[i] * roman[i]
print(sum)


from collections import Counter
b = Counter(s)
print(b)

for i in b:
	print(b[i])

a = [3, 2, 1]
b = [3, 2, 1]
print(a == b)


a, b = None, 15
if not a and not b:
	print("dfe")


player = [2, 1, 4, 8, 3]
indx = 1
mylist = []
for p in player:
	mylist.append([p, indx])
	indx += 1
mylist.sort(key = lambda my:my[0], reverse = True)
indx = 1
for p in mylist:
	p.append(indx)
	indx += 1
mylist.sort(key = lambda my:my[1])
out = []
for p in mylist:
	if p[2] == 1:
		out.append("Gold Medal")
	elif p[2] == 2:
		out.append("Silver Medal")
	elif p[2] == 3:
		out.append("Bronze Medal")
	else:
		out.append(str(p[2]))
print(out)

s = "ddddcccda"

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
   """
    mydict = {}
    for letter in s:
        if letter in mydict:
            mydict[letter] += 1
        else :
            mydict[letter] = 1
    print(mydict)
    n = list(mydict.values()).index(1) if 1 in list(mydict.values()) else -1
    print(n)
    if n == -1:
        return -1
    else:
        return s.index(list(mydict.keys())[n])
a = firstUniqChar(s)
print(a)

str = "fjeijöl"
print(str.isupper())
print(str.islower())
print(str.istitle())
print(str[2:].isupper())
print(str.istitle())  # determine if it is a title, first letter upper and following lower letters.

nums = [3,3,4]
dictor = {}
ind = 0
for i in nums:
    dictor[i] = ind
    ind += 1
			
print(dictor)
target = 6

for n in range(len(nums)):
    if target - nums[n] in dictor and dictor[nums[n]] != dictor[target - nums[n]]:
        print( dictor[nums[n]], dictor[target - nums[n]])
    if target - nums[n] in dictor:
        print(dictor[nums[n]], dictor[target - nums[n]])

for i,j in enumerate(nums):   # enumerate 
	print(i,j)
print(list(enumerate(nums, 2)))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(4)
tempL = TreeNode(2)
tempR = TreeNode(7)
root.left = tempL
root.right = tempR
tempL = TreeNode(1)
tempR = TreeNode(3)
root.left.left = tempL
root.left.right = tempR
print(root.left.left.val)
a = root.left
print(a.val)
print(a.left.val)