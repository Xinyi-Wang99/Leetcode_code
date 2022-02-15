# 141. Linked List Cycle 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# My Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the pos is not a parameters, its a parameter to construct the linked list
 
        if not head:
            return False
        s = set()
        temp = head
        while temp.next!= None:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False
        

# Insights:
# Some peopel are using the runner and walker example