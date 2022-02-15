# 206. Reverse Linked List 
# Author: Xinyi Wang
# Email: Xinyi.Wang9903@gmail.com

# Question Description:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# My thoughts: reverse the arrow direction

# My Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # if there's no elements or only one elements in the linked list
            return head
        else:
            # at least 2 value
            current = head.next
            result = head
            result.next = None
            while current:
                temp = current
                current = current.next
                temp.next = result
                result = temp
            return result

# Other people solution:
    def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            cur, prev = head, None
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            return prev


# Recursive call:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            # how to call a recursive function 
            node = self.reverseList(head.next)   
            # head.next is the next node and then then its link to the previous node
            head.next.next = head
            head.next = None
            return node
            # pay attention to where to use node and where to use head

    # I think for the recursive, its a devide-and-congure algorithm.
    # the basic idea is first to devide them and then combine them together