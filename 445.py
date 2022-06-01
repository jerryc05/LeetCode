from listnode import *


def f(l1: ListNode, l2: ListNode) -> 'ListNode|None':
    n1 = 0
    n2 = 0
    while l1 is not None:
        n1 = 10 * n1 + l1.val
        l1 = l1.next
    while l2 is not None:
        n2 = 10 * n2 + l2.val
        l2 = l2.next
    n = n1 + n2
    dummy = ListNode()
    while n > 0:
        dummy.next = ListNode(n % 10, dummy.next)
        n //= 10
    return dummy.next if dummy.next is not None else ListNode()


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        assert l1
        assert l2
        return f(l1, l2)


pp(
    f(
        ListNode(7, ListNode(2, ListNode(4, ListNode(3)))),
        ListNode(5, ListNode(6, ListNode(4))),
    )
)


pp(
    f(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4))),
    )
)


pp(
    f(
        ListNode(0),
        ListNode(0),
    )
)
