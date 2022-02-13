# 383. Ransom Note 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# My thoughts:
# 1. At the very begining, I thought I could count how many times the letter shows up in the ransomNote and how many times
#    the letter shows in the magazine, compare the times and then decide wether its True or False

# 2. After implementing some of those, I think maybe the better idea is counting either magazine or ransomeNote, and then itereate
#    another string to decrease the counted number(a little bit difference between counting magazine or ransomNote).

# My Solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = set(magazine)
        magaDict = dict.fromkeys(maga,0)
        for alpha in magazine:
            magaDict[alpha] += 1
        for alpha in ransomNote:
            if alpha not in magaDict:
                return False
            else:
                if magaDict[alpha] == 0:
                    return False
                else:
                    magaDict[alpha] -= 1
        return True

# Learning:
# collections.Counter() --- a dict subclass for counting hashable objects. It is a collection where elements are stored as
# dictonary keys and their counts are stored as dictionary values. 
# after testing, we HAVE to make sure the order is collections.Counter(ransomNote) - collections.Counter(magazine)
# it will return an empty collection, if the second one is greater than the first collections


# Some learning with Counter:
# 1. elements()     
# 2. most_common()
# 3. subtract()
# 4. total()
# if we do counter(A) | counter(B) it will return the max(a[x], b[x])

