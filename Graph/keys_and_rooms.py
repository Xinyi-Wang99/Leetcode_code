# 841. Keys and Rooms 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. 
# However, you cannot enter a locked room without having its key.When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit 
# all the rooms, or false otherwise.

# My thoughts:
# Bying recursive calls to see if all rooms can be opened.

# My Solution:
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def checkLocked( key:int , rooms: List[List[int]], locked:List[bool]):
            if not locked[key]:
                return locked
            else:
                locked[key] = False
                room = rooms[key]
                if not room:
                    return locked
                for key in room:
                    # here we need to store the new version of locked 
                    locked = checkLocked(key, rooms, locked)
                return locked
                
        locked = [True for i in range(len(rooms))]
        locked[0] = False
        room = rooms[0]
        if not room and len(room) > 1:
            return False
        for key in room:
            print(key)
            locked = checkLocked(key, rooms, locked)
        return False if True in locked else True

# Other people's solution:
# Using DFS to see if all rooms can be opened
 def canVisitAllRooms(self, rooms):
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms): return True
        return len(seen) == len(rooms)