from listnode import *


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head2 = head
        head = head.next
        assert head
        head2.next = self.swapPairs(head.next)
        head.next = head2
        return head


print(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


print(Solution().swapPairs(ListNode(1)))
