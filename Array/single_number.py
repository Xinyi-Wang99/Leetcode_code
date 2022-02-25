# 136. Single Number 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# My thought:
# At the very beginning, I don't have any idea about how to do that. But that's an easy question and it requires has 
# O(n) time complexity and only can have constant extra space. I believe it must have a really easy way to solve it.
# After seeing the discussion that realized this is a bitwise operation. It's using XOR operation

# Bitwise operator review:
# x & y -- and
# x | y -- or
# ~ x -- complement of x
# x ^ y -- exclusive or (if it has an odd number of 1s, it will return 1)
# x >> y -- make x right shift y digits like 00110110 >> 3 = 00000110 
#           the number will go down and basically its like drop off the last y digits
# x << y -- make x left shift y digits like 00110110 << 3 = 00110110000
#           the number will go up and basically its like adding y tralling 0s after x

# In this case, we should use the exclusive or, because only one number shows up once and all of the others shows up twice. 
# If we do exclusive or continously, the two number that are the same will cancel up. Finally, it would only show the number
# who shows up once

# My Solution;
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if we initialize the single to nums[1], then we have to make sure we iterate
        # from the second number in the array
        single = 0
        for num in nums:
            single = single ^ num
        return single