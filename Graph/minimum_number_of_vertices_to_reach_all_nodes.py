# 1557. Minimum Bumber of Vetices to Reach All Nodes 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] 
# represents a directed edge from node fromi to node toi. Find the smallest set of vertices from which all nodes in the 
# graph are reachable. It's guaranteed that a unique solution exists. Notice that you can return the vertices in any order.

# the key point to solve this problem is find the vertex doesnt have the indegree

# My Solution:
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        if not list:
            return [i for i in range(n)]
        indegree = set()
        for edge in edges:
            indegree.add(edge[1])
        allV = set([ i for i in range(n)])
        return list(allV - indegree)
        
