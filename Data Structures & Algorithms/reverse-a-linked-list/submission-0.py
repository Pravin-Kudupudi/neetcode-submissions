# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #1

            temp = curr.next #store 1
            curr.next = prev 
            prev = curr
            curr = temp
        
        return prev

        
