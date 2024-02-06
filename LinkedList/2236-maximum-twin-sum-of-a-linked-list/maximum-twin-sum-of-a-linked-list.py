# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        slow.next=None
        maxi=0
        head1, head2 = head, prev
        while head1 and head2:
            value=head1.val+head2.val
            maxi=max(maxi,value)
            head1=head1.next
            head2=head2.next
        return maxi
        # Time Complexity O(n)
        # Space Complexity O(1)
        
