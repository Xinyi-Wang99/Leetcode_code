# 387. First Unique Character in a String 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# My thoughts:
# iterate the reversed string and count the repeated number, and update their indices, so once we find if there is a charaacter
# only shows once, then we can compare their indiex and decide if we want or not

# My Solution:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueS = set(s)
        # initialize a dictionary with the initial value
        counter = dict.fromkeys(uniqueS, 0)
        indexcur = dict.fromkeys(uniqueS, len(s))
        # reversed a string
        # reversedS = s[::-1]
        # reverse for loop
        # pay attention that when we use range, it only covers the start point not the end point
        for index in range(len(s)-1,-1,-1):
            counter[s[index]] = counter[s[index]] + 1
            indexcur[s[index]] = index
        value = len(s)
        for alpha, counter in counter.items():
            if counter == 1:
                if indexcur[alpha] < value:
                    value = indexcur[alpha]
        # python ternary operator
        return -1 if value == len(s) else value

# Other Solution:
# Author: etherealoptimist
class Solution:
    def firstUniqChar(self, s):
        d = {}
        seen = set()
        # I think this is really smart. Once the letter shows again, we dont care anymore. 
        # Since we want the first unique, so we stored the index from the begining 
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1
