# 104. Maximum Depth of Binary Tree
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# My thoughts:
# 1. using BFS to get the layer number but I think it's not too efficient?
# 2. write a recursive call calculate the layer number

# My Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
    
    
