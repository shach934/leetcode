399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # use a directed weighted graph to record all the equations and relations.
        # Then use dfs to find a path connect the two nodes quiried. 
        def dfs(G, a, b, accum, seen):
            option = G[a]
            for op in option:
                if op[0] == b:
                    return accum*op[1]
                if op not in seen:
                    seen[op] = 1
                    ret = dfs(G, op[0], b, op[1], seen)
                    if ret is not None:
                        return accum*ret
            return None

        G = {}
        for idx in range(len(values)):
            if equations[idx][0] not in G:
                G[equations[idx][0]] = set()
                G[equations[idx][0]].add((equations[idx][1], values[idx]))
            else:
                G[equations[idx][0]].add((equations[idx][1],values[idx]))
            if equations[idx][1] not in G:
                G[equations[idx][1]] = set()
                G[equations[idx][1]].add((equations[idx][0], 1.0/values[idx]))
            else:
                G[equations[idx][1]].add((equations[idx][0],1.0/values[idx]))
        ans = []
        for i in queries:
            if i[0] not in G or i[1] not in G:
                ans.append(-1.0)
            elif i[0] == i[1] and i[0] in G:
                ans.append(1.0)
            else:
                ret = dfs(G, i[0], i[1], 1, {})
                if ret is not None:
                    ans.append(ret)
                else:
                    ans.append(-1.0)
        return ans