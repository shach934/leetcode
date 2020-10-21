"""
KMP Algorithm. 
find if B is a substring in A.
The algorithm discribe as follow:
First preprocess the string to look for, construct a next list.
This list has the same length as string B, on each position i, it record the longest same surfix and prefix of the substring B[:i]
Then shift this next to right for one postion, put -1 in the first.

Second, go through A and B with i, j, if A[i] == B[j], i ++ , j++, else if next[j] is -1, i++, else,
keep i, and j go to next[j]
until i reach the end of j reach the end, if j reach the end, means there is match.
"""

A = 'BBC ABCDAB ABCDABCDABDE'
B = 'ABCDABD'

def get_next(B):
    next = [-1]
    k, j = -1, 0
    while j < len(B) - 1:
        if k == -1 or B[j] == B[k]:
            k += 1
            j += 1
            next.append(k)
        else:
            k = next[k]
    return next

def KMP(A, B):
    next = get_next(B)
    i,j = -1, -1
    while i < len(A) and j < len(B):
        if next[j] == -1 or A[i] == B[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(B):
        return i - j
    else:
        return -1
a = KMP(A, B)
print(a)