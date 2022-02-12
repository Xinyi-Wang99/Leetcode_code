#74. Search a 2D matrix 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# My Solution:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        # the smallest number in the matrix
        if target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False
        else:
            current = 0
            for num, row in enumerate(matrix):
                if row[0] == target or row[col-1] == target:
                    return True
                elif row[0] <target:
                    current = num
            for num in matrix[current]:
                if num == target:
                    return True
            return False

# basically find which row could have the goal, and then search that row

# Insights from others:
# 1. Dont treat this as a 2D array, just treat it as a sorted list, and use the bineray search. Dont be distracted by the format
#    focus on the data structure
# 2. here is one of the python format:  rows, cols = len(matrix), len(matrix[0])
# 3. bisect() provides support for maintaining a list in sorted order without having to sort the list after each insertion
#    but this is a library that needs to import 