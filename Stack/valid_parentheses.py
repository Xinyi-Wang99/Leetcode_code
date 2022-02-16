# 20. Valid Parentheses 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.

# At the very begining, I ddidnt realize the point to use the stack, I thought all the parentheses would save in the string
# one by one, so we can iterate the string by size two and make sure the next one is one of the pair of previous one 
# then I met this case `{()}` this should also return true

# Finally realized the point of FIRST IN, LAST OUT  

# The corner cases I met: 
#    1. "{[]}"
#    2. "(("

# My Final Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 == 1:
            return False
        else:
            stack = []
            pair = {')': '(', '}': '{', ']': '['}
            for char in s:
                if char in pair.values():
                    stack.append(char)
                else:
                    if not stack:
                        return False
                    if stack.pop() != pair[char]:
                        return False
            if stack:
                return False
            return True