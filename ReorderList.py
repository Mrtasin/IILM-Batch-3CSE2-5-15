# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if (head.next == None) or (head.next.next == None):
            pass
        else:
            sp = fp = head
            while fp.next and fp.next.next:
                sp = sp.next
                fp = fp.next.next
            temp = sp.next
            sp.next = None
            start = None
            while temp:
                tm = temp
                temp = temp.next
                tm.next = start
                start = tm
            temp = start

            start = end = head
            head = head.next
            end.next = None

            while head and temp:
                tm = temp
                temp = temp.next
                tm.next = None
                end.next = tm
                end = tm
                tm = head
                head = head.next
                tm.next = None
                end.next = tm
                end = tm

            end.next = temp

            head = start
