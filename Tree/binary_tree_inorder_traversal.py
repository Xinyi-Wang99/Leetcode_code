# 94. Binary Tree Inorder Traversal 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return the inorder traversal of its nodes' values. (inorder would be left, root, right)

# I didnt come up a solution by using stack
# Here's other people's solution:

# iteratively
# come from autekwing
      
def inorderTraversal(self, root):
    rest, stack = [],[]
    while stack or root:
        if root:
            stack.append(root)
            root = root.left    # since this is inorder, so the left node should be ahead of the root
                                # it's need to add after the root
        else:
            current = stack.pop()
            rest.append(current.val)
            root = current.right    # this is because if we get the current node from the stack,
                                    # all itself and its left child has already been stored into stack
                                    # so we need to start checking its right child
    return rest