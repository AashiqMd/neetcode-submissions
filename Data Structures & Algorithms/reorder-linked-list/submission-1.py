# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]: 
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            return prev
        
        head1, head2 = head, reverseList(slow.next)
        slow.next = None

        while head2:
            t1, t2 = head1.next, head2.next
            head1.next, head2.next = head2, t1
            head1, head2 = t1, t2