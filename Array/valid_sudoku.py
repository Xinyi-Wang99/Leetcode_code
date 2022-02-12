# 36. Valid Sudoku
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# My thoughts:
# My first thought would be using `set` to check if there's any repetiton, but then I realized that the '.' would influence the length,
# so this can't work. 

# However:
#     eg: a = set([1,2,3]) could convert a list to a set, if they have the same length, then all elements are unique

# Other Solution:
def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    # zip() functin takes iterables, aggregates them in a tuple and return it
    # eg: a = ['A','B','C']
    #     b = ['a','b','c']
    #     c = zip(a, b)    
    #     print(tuple(c))   using tuple() to display a readiable version of the result
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True
    
def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    # first remove all the dot and then use set
    # remove something that is less important but will confuse the output
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)


# Other thing I learned:
# enumerate( an iterator): can automatically add the index
# e.g: for i, j in enumerate([a, b, c]):
#          print(i, j)                  // 0, a        1, b        2, c
# you can also add a start point, like this: enumerate([a, b. c], start = 2) then i would start as 2