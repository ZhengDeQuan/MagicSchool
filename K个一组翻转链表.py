from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        temp_num = 1
        while cur:
            if temp_num == k:
                this_seg_start ,this_seg_end = self.reverse(pre_head=pre , next_seg_start = cur.next)
                # print("ys")
                # Print(this_seg_start)
                pre=this_seg_end
                cur = pre.next
                temp_num = 1
            else:
                temp_num += 1
                cur = cur.next
        return dummy.next


    def reverse(self , pre_head , next_seg_start):
        '''
        reverse head -> ... ->tail to tail-> ...->head
        pre_head -> head
        不断的网pre_head.next处插入循环的节点
        '''
        this_seg_last = pre_head.next#this_seg_last的指向从此之后没有改变过，但是this_seg_last.next的指向就是时时变化着的
        cur = pre_head.next.next
        while cur != next_seg_start:
            this_seg_last.next = cur.next

            cur.next = pre_head.next
            pre_head.next = cur

            cur = this_seg_last.next

        return pre_head.next, this_seg_last

def makeListNodes(List):
    Head = ListNode(-1)
    cur = Head
    for ele in List:
        cur.next = ListNode(ele)
        cur = cur.next
    return Head.next

def Print(Head):
    while Head:
        print(Head.val)
        Head = Head.next


if __name__ == "__main__":
    a = [1,2,3,4,5]
    Head = makeListNodes(a)
    A = Solution()
    res = A.reverseKGroup(Head,2)
    Print(res)





