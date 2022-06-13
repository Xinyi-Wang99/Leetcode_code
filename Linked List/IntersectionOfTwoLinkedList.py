class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aLength = 0
        while headA.next != None:
            aLength += 1
        bLength = 0
        while headB.next != None:
            bLength += 1
        # difference > 0 => a is longer than b
        # difference < 0 => b is longer than a 
        difference = aLength - bLength
        longer = headA
        shorter = headB
        if difference < 0:
            longer = headB
            shorter = headA
        while difference > 0:
            longer = longer.next
            difference -= 1
        intersectVal = None
        while shorter.next != None:
            if shorter.val == longer.val:
                intersectVal = shorter.val
            else:
                intersectVal = None
        if intersectVal is not None:
            return f'Intersected at \'intersectVal\''
        else:
            return 'No intersection'

        

