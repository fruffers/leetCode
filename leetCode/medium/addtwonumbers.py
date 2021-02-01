# .2 Add two numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # add two numbers from sum of both linked lists in reverse order
        # initalise pointers for reversal of linkedlist
        # get sum of first
        l1 = self.reverse(l1)
        sum1 = self.adder(l1)
        # get sum of second
        l2 = self.reverse(l2)
        sum2 = self.adder(l2)
        # add together
        tog = (str(int(sum1)+int(sum2)))[::-1]
        # make a new ll
        ll = ListNode(tog[0])
        head = ll
        for i in range(1,len(tog)):
            ll.next = ListNode(tog[i])
            ll = ll.next
        return head
        
    def reverse(self,head):
        prev = None
        curr = head
        nexta = None
        suma = ""
        suma+=str(head.val)
        while curr != None:
            # store next
            nexta = curr.next
            # make current->next to prev
            curr.next = prev
            # move prev and cur up
            prev = curr
            curr = nexta
        head = prev
        return head
    
    def adder(self,head):
        suma = str(head.val)
        while head.next != None:
            head = head.next
            suma += str(head.val)
        return suma
