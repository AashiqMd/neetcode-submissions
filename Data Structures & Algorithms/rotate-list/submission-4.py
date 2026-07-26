# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head

        # Length pass
        len = 0
        if head is not None:
            temp = head
            while temp is not None:
                len+=1
                temp = temp.next

        k = k%len
        if k == 0:
            return head

        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead