# 98. Validate Binary Search Tree 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# I didnt come up the solution at the very begining untill saw the discussion 

# Insights:
# 1. Do not seperate each question. Like the validate, you still need to go over all tree to make sure the node soted
# as we want. Therefore, it can be converted to a traversal problem

# 2. Read the problem carefully! like `less than` not `less or equal`

# 3. Do not try to memorize the solution, understand how it works and write by yourself

# Solutions:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # solve it by inorder traversalFG
        stack= []
        pre = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root:
                    if pre:
                        if pre.val >= root.val:
                            return False
                    pre = root
                    root = root.right
        return True