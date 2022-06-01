from listnode import *

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(None, head)
        it=dummy
        while it is not None:
            while it.next is not None and it.next.next is not None and it.next.val==it.next.next.val:
                it.next=it.next.next
            it=it.next
        return dummy.next



pp(Solution().deleteDuplicates(
    ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(2)))))
))



pp(Solution().deleteDuplicates(
    ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
))