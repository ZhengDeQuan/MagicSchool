import sys
import bisect

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        NewHead = ListNode()
        curNew = NewHead
        TempHead = None
        cur = head
        while cur!=None:
            TempHead , cur , flag = self.findOneGroup(cur,k)
            if flag == False:
                curNew = TempHead
                break
            else:
                curTemp = TempHead
                while k >0:
                    k-=1
                    temp = curTemp
                    temp.next = curNew.next
                    curNew.next = temp
                    curTemp = curTemp.next

        return curNew

    def findOneGroup(self , head , k):
        cur = head
        while cur!=None and k!=0:
            cur = cur.next
            k-=1
        if k==0:
            return head,cur,True
        return head , cur , False
