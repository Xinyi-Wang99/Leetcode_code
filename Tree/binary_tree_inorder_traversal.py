# 94. Binary Tree Inorder Traversal 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return the inorder traversal of its nodes' values. (inorder would be left, root, right)

# I didnt come up a solution by using stack
# Here's other people's solution:

# iteratively
# come from OldCodingFarmer
      
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right