# 406. Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key = lambda x: (x[0], -x[1]), reverse = True)
        for i in range(len(people)):
            temp, idx, count = people[i], i-1, i
            while idx >= 0 and count != temp[1]:
                if people[idx][0] >= temp[0]:
                    count -= 1
                else:
                    count += 1
                people[idx+1] = people[idx]
                idx -= 1
            people[idx+1] = temp
        return people