from listnode import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        it = dummy
        while it is not None:
            if (
                it.next is not None
                and it.next.next is not None
                and it.next.val == it.next.next.val
            ):
                while it.next.next.next is not None and it.next.val == it.next.next.next.val:
                    it.next.next = it.next.next.next
                it.next = it.next.next.next
            else:
                it = it.next
        return dummy.next


pp(
    Solution().deleteDuplicates(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
    )
)


pp(
    Solution().deleteDuplicates(
        ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    )
)
