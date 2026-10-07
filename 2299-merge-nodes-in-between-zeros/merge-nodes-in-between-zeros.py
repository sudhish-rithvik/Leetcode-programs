class Solution(object):
    def mergeNodes(self, head):
        dummy = ListNode(0)
        tail = dummy

        curr = head.next
        total = 0

        while curr:
            if curr.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += curr.val

            curr = curr.next

        return dummy.next