# 169. Majority Element 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# My thought:
# counting for each element and then return if one of the frequency is greater than n/2
# but the time complexity is O(n) and the space complexity is O(n) as well

# Other people thought:
# 1. sort the array and return the element that in the middle of array. then time complexity
# is O(nlog)
# 2.'fast majority vote' problem:
#   thinking we are trying to vote a president. We are counting for the polls, increase 1 if there's
#   someone vote for him and decrease 1 if there's some one vote for others. Then return the final person
#   The reason why it would work because we assume there's always someone who has more than n/2 tickets.

# Solution:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count = count + 1
            else:
                count = count - 1
        return majority
        