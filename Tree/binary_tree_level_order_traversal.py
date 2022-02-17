# 144. Binary Tree Level Order Traversal 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# My Solution(I think its pretty straightforward):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            current = [root]
            result = []
            while len(current) > 0:
                nextLine = []
                currentValue = []
                for node in current:
                    if node:
                        currentValue.append(node.val)
                    # the reason to adding if node.left and if node.right check is to avoid
                    # they add None to nextLine
                    if node.left:
                        nextLine.append(node.left) 
                    if node.right:
                        nextLine.append(node.right)
                result.append(currentValue)
                current = nextLine
            return result
                
        