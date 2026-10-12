# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        #use the copy of list1 and list2 to keep original list at the head node
        l1 = list1
        l2 = list2

        #find the first element
        if l1.val <= l2.val:
            merged_list = ListNode(l1.val)
            l1 = l1.next
        else:
            merged_list = ListNode(l2.val)
            l2 = l2.next
        
        #track current node of the merged list
        cur = merged_list
        
        #iterate l1 and l2 
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next   

        #iterate the remaining list
        while l1:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next     
        while l2:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next    

        return merged_list     
