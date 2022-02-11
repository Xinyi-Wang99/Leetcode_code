# 118. Pascal's Triangle
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

# My solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            first = [1]
            second = [1,1]
            data = [first,second]
            for i in range(3, numRows+1):
                #initial a list
                current = [1] * i
                for j in range(1, i-1):
                    current[j] = data[i-2][j-1] + data[i-2][j]
                data.append(current)
            return data

# Notice:
# 1. if the index out of range
# 2. adding an element to a list should use `append`
# 3. initialize a list can do `[1] * the number of entries`

# better way to implemented:
#     since it's highly symmetric, the current list = appending an zero to the previous list and adding its reverse version
# e.g:
# [1, 4, 6, 4, 1] = [1, 3, 3, 1, 0] + [0, 1, 3, 3, 1]