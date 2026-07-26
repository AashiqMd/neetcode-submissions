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
        # fast = head

        # Length pass
        length = 1
        tail = head
        while tail.next:
            length+=1
            tail = tail.next

        k = k%length
        if k == 0:
            return head

        # for _ in range(k):
        #     fast = fast.next
        
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        
        for _ in range(length - k - 1):
            slow = slow.next

        newHead = slow.next
        slow.next = None
        tail.next = head

        return newHead