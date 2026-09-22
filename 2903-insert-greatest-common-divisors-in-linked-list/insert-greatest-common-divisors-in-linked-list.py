class Solution(object):
    def insertGreatestCommonDivisors(self, head):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head

        while curr and curr.next:
            next_node = curr.next

            g = gcd(curr.val, next_node.val)

            new_node = ListNode(g)
            curr.next = new_node
            new_node.next = next_node

            # Move to the original next node
            curr = next_node

        return head