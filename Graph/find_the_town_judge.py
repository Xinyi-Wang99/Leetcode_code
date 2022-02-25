# 997. Find the Town Judge
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
#  1. The town judge trusts nobody.
#  2. Everybody (except for the town judge) trusts the town judge.
#  3. There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


# This is a problem that not only cares about the indeg but also outdeg.

# My solution:
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n ==1 else -1
        judge = [[0,0] for i in range(0,n+1)]
        #(in, out)
        for name, trusted in trust:
            judge[name][1] = 1 + judge[name][1]
            judge[trusted][0] = 1 + judge[trusted][0]
        candidates = []
        for index, people in enumerate(judge):
            if people[0] == n - 1 and people[1] == 0:
                candidates.append(index)
        return candidates[0] if len(candidates) == 1 else -1

# My way is store the indegree and outdegree seperately. However, a better way is store them together, if there's a coming edge
# then we add 1, and if there's an outgoing edge, we minus 1

# other people's solution: 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
        # but I think maybe here we might want to add another check
        # to see if there's only one node that Trusted[i] == N-1 
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1