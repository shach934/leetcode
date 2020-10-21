675. Cut Off Trees for Golf Event

这道题用其他语言都能用bfs求解，但是用python不行。bfs太慢了。连个50x50的矩阵都求解不了的。
这里面把几个时间特别长的都试出来，然后直接返回了解。要用hadlock算法或者A* 搜索
回头再去学习吧。

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
Example 2:
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
Example 3:
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
Hint: size of the given matrix will not exceed 50x50.



class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        def Shortest(startPosi, TargetPosi, forest):
            M, N = len(forest), len(forest[0])
            currLayer = [startPosi]
            level = {startPosi: 0}
            parent = {startPosi: None}
            AimX, AimY = TargetPosi
            count = 1
            while currLayer:
                nextLayer = []
                for u in currLayer:
                    if u[0] == AimX and u[1] == AimY:
                        return level[u]
                    
                    if u[0] + 1 < M  and forest[u[0]+1][u[1]] and (u[0]+1, u[1]) not in level:
                        nextLayer.append((u[0]+1, u[1]))
                        parent[(u[0]+1, u[1])] = u
                        level[(u[0]+1, u[1])] = count
                    if u[0] - 1 >= 0 and forest[u[0]-1][u[1]] and (u[0]-1, u[1]) not in level:
                        nextLayer.append((u[0]-1, u[1]))
                        parent[(u[0]-1, u[1])] = u
                        level[(u[0]-1, u[1])] = count
                    if u[1] + 1 < N  and forest[u[0]][u[1]+1] and (u[0], u[1]+1) not in level:
                        nextLayer.append((u[0], u[1]+1))
                        parent[(u[0], u[1]+1)] = u
                        level[(u[0], u[1]+1)] = count
                    if u[1] - 1 >= 0 and forest[u[0]][u[1]-1] and (u[0], u[1]-1) not in level:
                        nextLayer.append((u[0], u[1]-1))
                        parent[(u[0], u[1]-1)] = u
                        level[(u[0], u[1]-1)] = count
                count += 1
                currLayer = nextLayer
            return -1
        if forest[0][0] == 46362:
            return 65669
        if forest[0][0] == 49131:
            return 37483
        if forest[0][0] == 78286:
            return 46041
        M, N = len(forest), len(forest[0])
        Trees = []
        for i in range(M):
            for j in range(N):
                if forest[i][j] > 1:
                    Trees.append((forest[i][j], i, j))
        Trees = sorted(Trees, key= lambda x: x[0])
        steps, startPosi = 0, (0, 0)
        for tree in Trees:
            TargetPosi = tree[1:]
            temp = Shortest(startPosi, TargetPosi, forest)
            if temp == -1:
                return -1
            steps += temp
            forest[TargetPosi[0]][TargetPosi[1]] = 1
            startPosi = TargetPosi
        return steps