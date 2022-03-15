# 15. 3Sum 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# My thoughts:
# 1. sort the whole array, if the smallest number is greater than zero, then it can't 
# have the solution. The same can be obtained, if the largest number is less than zero.
# No solution, either

# 2. Then we can split the array into two parts, one is all negative numbers, and the other
# is all the left. The tuple must have at least 1 number in each arry, and at most two.

# We could iterate all numbers in the whole array(positive and negative) and find if 
# there's any number in the opposite way can add together to equal to its negative.
# If so, we find a result 

# My solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3 or nums[0] > 0 or nums[len(nums)-1] < 0:
            return []
        # if we just say they are target, then we dont need to care how many of them
        # we can use set to avoid the same numbers
        negative = set()
        positive = set()
        bound = -1
        # count the number of zeros, if its greater than 3, then add a (0,0,0) to the results
        zero = 0
        for num in nums:
            if num < 0:
                bound = bound + 1
                negative.add(num)
            elif num > 0:
                positive.add(num)
            else:
                zero = zero + 1
        result = []
        
        for num in negative:
            previous = nums[0]
            for index in range(bound+1, len(nums)):
                # since we are finding the results from the whole array,
                # but if the target is the same, we can skip the one if
                # its the same as the previous
                # eg:[-4,2,2,2]
                # -4 is the targer, we would find the result is (-4,2,2)
                # but we dont need to based on the second 2 to find the result again
                if nums[index] == previous:
                    continue
                previous = nums[index]
                need = -(num + nums[index])
                if need < 0:
                    break
                else:
                    if need in nums[index+1:]:
                        result.append([num,nums[index], need])
                        
        for num in positive:
            previous = nums[len(nums)-1]
            for index in range(bound, 0, -1):
                if nums[index] == previous:
                    continue
                previous = nums[index]
                need = -(num + nums[index])
                if need > 0:
                    break
                else:
                    if need in nums[0: index]:
                        result.append([num, nums[index], need])
        if zero > 2:
            result.append([0,0,0])
        return result

        #poor thing is TIME LIMIT EXCEEDED
        #O(n^2)

# after seeing the discussion, I think the basic idea is correct, but for the detailed
# implementation. They are doing better than me.

# actually, no. They're idea is so much better than me


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we immediately return if its less than 3 numbers
        if len(nums) < 3:
            return []
        nums.sort()
        results = []
        for i in range(len(nums)-1):
            # we want to these 3 numbes adding together is equal to zero
            # nums[i] is the smallest number in the current tuple(if exists),
            # so if the samllest number is greater than zero and the array has
            # been sorted already, we dont have to check the rest of them
            if nums[i] > 0:
                break
            # I'd like to use a previous variable to store it
            # but I think this is a better idea, no matter what, we have to use 
            # an if condition, why bother to waste a space to store the `previous`
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l , r = i+1, len(nums) -1   #start all from the right side of the target
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # I do think this is a really smart way to implement like this
                # it can avoid duplicate and also out of the index
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    results.append([nums[l], nums[r], nums[i]])
                    # once we have found one result based on the current target,
                    # we should keep finding until those two pointers meet together
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    # why this would work?
                    # this while loop stop at the last same number
                    # and we have an extra `l += 1 ` after this 'extra'
                    # `l += 1 `, the pointer will point to the next unique
                    # number, same as r
                    l += 1
                    r -= 1
        return results


