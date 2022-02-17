# 144. Binary Tree Preorder Traversal 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# My thought:
# Using recursion to iterate all of them, since the order root, left, right. 

# My solution:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return root
        else:
            return self.traversalResult(root,[])
        
        
    def traversalResult(self, root:Optional[TreeNode], result):

        result.append(root.val)
        
        if root.left:
            self.traversalResult(root.left, result)
        if root.right:
            self.traversalResult(root.right, result)
        
        return result
    
# Other Solution:
# using stack to help iterating
# some points I have missed at the very beginning: 
# 1. When we pass the item into the stack, we are not passing each number, we are passing a node.
# 2. As a node as a single element. 

#Other people's solution:
def preorderTraversal(self, root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            ret.append(node.val)
            #pay more attention here, the first node append to the stack its the right child
            stack.append(node.right)
            stack.append(node.left)
    return ret
