# 145. Binary Tree Preorder Traversal 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# My Solution:

# 1. Using recursive call, pretty easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root,result)
        return result
    
    def traversal(self, root, result):
        if root:
            self.traversal(root.left, result)
            self.traversal(root.right, result)
            result.append(root.val)

# 2. I had tried at least 2 hours to try to figure out how to iterate the binary tree by post order
#    Finally, I gave up I saw a really really smart way come from `OldCodingFarm`, which basically 
#    like reverse the preorder way.

#    However, preorder is: root, left, right
#             postorder is: left, right, root

# The way we can do is switch the position of which child goes to stack at first.
# Here is the code:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,res = [root], []
        while stack:
            node = stack.pop()
            if node:
                # reverse the order here, that is soooooo SMART!!!!!!!
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        return reversed(res)
            