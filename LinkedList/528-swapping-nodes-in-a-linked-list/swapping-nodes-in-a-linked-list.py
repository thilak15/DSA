# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        first=dummy
        last=dummy
        t=k
        n=0
        temp=head

        while t>1:
            first=first.next
            t-=1
        while temp:
            n+=1
            temp=temp.next
        r=n-k
        while r>0:
            last=last.next
            r-=1
        first.next.val,last.next.val=last.next.val,first.next.val
        return head
        
